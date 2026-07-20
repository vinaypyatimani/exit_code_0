#!/usr/bin/env python3
"""
update_log.py — appends today's commit(s) to LEARNING_LOG.md automatically.

Run by .github/workflows/daily-log.yml on every push to main.
Can also be run locally: `python scripts/update_log.py` after a commit,
if you want to update the log without waiting for the Action to run.

No third-party dependencies — stdlib only, so the Action needs no pip install.
"""
import json
import re
import subprocess
import sys
from datetime import date
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
CONFIG_PATH = REPO_ROOT / ".learning-config.json"
PROGRESS_PATH = REPO_ROOT / ".learning-progress.json"
LOG_PATH = REPO_ROOT / "LEARNING_LOG.md"
ROADMAP_PATH = REPO_ROOT / "ROADMAP.md"
TOTAL_DAYS = 60

STATS_START = "<!-- STATS_START -->"
STATS_END = "<!-- STATS_END -->"
LOG_START = "<!-- LOG_START -->"


def run(cmd: list[str]) -> str:
    return subprocess.check_output(cmd, cwd=REPO_ROOT, text=True).strip()


def load_json(path: Path, default: dict) -> dict:
    if not path.exists():
        return default
    return json.loads(path.read_text())


def save_json(path: Path, data: dict) -> None:
    path.write_text(json.dumps(data, indent=2) + "\n")


def get_config() -> dict:
    cfg = load_json(CONFIG_PATH, {})
    if "start_date" not in cfg:
        # First run ever: today becomes Day 1. Edit .learning-config.json
        # if you actually started earlier and are backfilling.
        cfg["start_date"] = date.today().isoformat()
        save_json(CONFIG_PATH, cfg)
    return cfg


def compute_day_number(start_date_str: str) -> int:
    start = date.fromisoformat(start_date_str)
    return max(1, (date.today() - start).days + 1)


def get_commit_info() -> dict:
    sha = run(["git", "log", "-1", "--pretty=%h"])
    subject = run(["git", "log", "-1", "--pretty=%s"])
    stat = run(["git", "show", "--stat", "--pretty=format:", "HEAD"])
    lines = [l for l in stat.splitlines() if l.strip()]
    summary = lines[-1].strip() if lines else "no file changes detected"
    files_changed = len([l for l in lines[:-1] if "|" in l])
    return {"sha": sha, "subject": subject, "summary": summary, "files_changed": files_changed}


def get_roadmap_title(day_n: int) -> str | None:
    if not ROADMAP_PATH.exists():
        return None
    text = ROADMAP_PATH.read_text()
    # Matches headers like "### Day 12 — Title" or "### Day 35–36 — Title"
    pattern = rf"^###\s*Day\s+{day_n}\b[^\n—-]*[—-]\s*(.+)$"
    match = re.search(pattern, text, re.MULTILINE)
    return match.group(1).strip() if match else None


def default_log_body() -> str:
    return (
        "# 📓 Learning Log — AI Engineer Transition\n\n"
        f"{STATS_START}\n_stats will appear here after your first logged commit_\n{STATS_END}\n\n"
        f"{LOG_START}\n"
    )


def split_log(text: str) -> tuple[str, str]:
    """Returns (header_before_LOG_START_inclusive, entries_after)."""
    idx = text.find(LOG_START)
    if idx == -1:
        text = default_log_body()
        idx = text.find(LOG_START)
    header = text[: idx + len(LOG_START)]
    entries = text[idx + len(LOG_START) :]
    return header, entries


def render_stats(progress: dict, day_n: int) -> str:
    completed = len(progress["days"])
    width = 30
    filled = int(width * min(day_n, TOTAL_DAYS) / TOTAL_DAYS)
    bar = "█" * filled + "░" * (width - filled)
    streak = progress.get("streak", 0)
    total_commits = progress.get("total_commits", 0)
    return (
        f"**Day {day_n} / {TOTAL_DAYS}** · Streak: {streak} 🔥 · "
        f"Days logged: {completed} · Total commits: {total_commits}\n\n"
        f"`[{bar}]`"
    )


def update_streak(progress: dict, today_str: str) -> None:
    days = sorted(progress["days"].keys())
    if not days:
        progress["streak"] = 1
    else:
        # Walk backward from today counting consecutive calendar days present.
        from datetime import timedelta

        streak = 0
        cursor = date.fromisoformat(today_str)
        day_set = set(days)
        while cursor.isoformat() in day_set:
            streak += 1
            cursor -= timedelta(days=1)
        progress["streak"] = streak
    progress["longest_streak"] = max(progress.get("longest_streak", 0), progress["streak"])


def main() -> None:
    cfg = get_config()
    day_n = compute_day_number(cfg["start_date"])
    today_str = date.today().isoformat()
    commit = get_commit_info()
    title = get_roadmap_title(day_n)

    progress = load_json(
        PROGRESS_PATH, {"days": {}, "streak": 0, "longest_streak": 0, "total_commits": 0}
    )
    progress["days"].setdefault(today_str, {"day_n": day_n, "commits": []})
    progress["days"][today_str]["commits"].append(commit["sha"])
    progress["total_commits"] = progress.get("total_commits", 0) + 1
    update_streak(progress, today_str)
    save_json(PROGRESS_PATH, progress)

    existing = LOG_PATH.read_text() if LOG_PATH.exists() else default_log_body()
    header, entries = split_log(existing)

    day_header = f"## Day {day_n} — {today_str}" + (f" — *{title}*" if title else "")
    bullet = f"- `{commit['sha']}` {commit['subject']} ({commit['summary']})"

    if entries.lstrip().startswith(f"## Day {day_n} —"):
        # Same day already has an entry: append this commit under it.
        first_break = entries.find("\n\n", entries.find(day_header))
        insert_at = entries.find("\n", entries.find(day_header)) + 1
        entries = entries[:insert_at] + bullet + "\n" + entries[insert_at:]
    else:
        entries = f"\n\n{day_header}\n{bullet}\n\n" + entries.lstrip("\n")

    new_stats_block = f"{STATS_START}\n{render_stats(progress, day_n)}\n{STATS_END}"
    new_header = re.sub(
        rf"{STATS_START}.*?{STATS_END}", new_stats_block, header, flags=re.DOTALL
    )
    if STATS_START not in new_header:
        new_header = new_header.replace(LOG_START, f"{new_stats_block}\n\n{LOG_START}")

    LOG_PATH.write_text(new_header + entries)
    print(f"Logged Day {day_n} ({today_str}), commit {commit['sha']}.")


if __name__ == "__main__":
    sys.exit(main())
