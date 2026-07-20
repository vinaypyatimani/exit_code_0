# 🚀 60 Days: Mediocre Dev → AI Engineer

A practical, project-first program to go from "strong software engineer, zero ML/AI background" to a portfolio that gets you interviews as an AI/GenAI engineer — in 60 days at 4+ hrs/day.

- **`ROADMAP.md`** — the day-by-day curriculum: what to learn, what to watch, what to read, and exactly what to build and commit each day.
- **`CERTIFICATIONS.md`** — a researched (not scraped-and-dumped) list of the certifications that actually move the needle, and which ones are dead or about to retire.
- **`LEARNING_LOG.md`** — updates itself. See below.

## The shape of the program
| Phase | Days | Focus |
|---|---|---|
| 0 — Foundations | 1–8 | Python for ML, math intuition, core ML vocabulary |
| 1 — Classical ML | 9–20 | Regression → trees → ensembles → clustering → a full Kaggle-style pipeline |
| 2 — Deep Learning | 21–32 | Neural nets from scratch → PyTorch → CNNs → RNNs |
| 3 — NLP & Transformers | 33–42 | Attention, build a GPT from scratch, fine-tune real models |
| 4 — GenAI/LLM Engineering | 43–56 | Prompting, RAG, vector DBs, LangChain/LlamaIndex, agents, fine-tuning, LLMOps |
| 5 — Capstone & Portfolio | 57–60 | Flagship project, portfolio polish, resume/LinkedIn, next steps |

By Day 60 you'll have **~55 committed projects** and 4–6 polished, deployed portfolio pieces (classical ML pipeline, computer vision app, fine-tuned NLP model, and a full RAG/agent application).

## Daily workflow
1. Open `ROADMAP.md`, find today's entry.
2. Do the reading/watching (30–60 min) — don't skip this, the projects go faster when you're not fighting the concepts.
3. Build today's project in a new folder: `dayNN-topic-slug/` with its own short `README.md`.
4. Commit and push to `main`.
5. That's it — `LEARNING_LOG.md` updates itself (see setup below).

Miss a day? Don't renumber anything — just pick up where you left off. The log tracks a streak, but a broken streak isn't a failed program.

---

## One-time setup: the auto-logger

This repo includes a GitHub Action that watches every push to `main` and automatically appends an entry to `LEARNING_LOG.md` — commit message, files changed, lines added/removed, and which roadmap day it maps to. You never type a log entry by hand.

**Setup (5 minutes):**
1. Create a new GitHub repo and push this entire folder to it (or `git init` here and add your own remote).
2. In the repo on GitHub: **Settings → Actions → General → Workflow permissions** → select **"Read and write permissions"** → Save. (Without this, the Action can't push the log update back.)
3. That's it. Your first commit becomes "Day 1" automatically. If you're backfilling and actually started a few days ago, edit `.learning-config.json` (created after your first push) and set `"start_date"` to the real date.

**How it works:** `.github/workflows/daily-log.yml` runs `scripts/update_log.py` on every push. The script is pure Python stdlib (no dependencies to install), reads your latest commit via `git`, looks up the matching day's title from `ROADMAP.md`, and updates `LEARNING_LOG.md` plus a small `.learning-progress.json` state file that tracks your streak. It commits the update back with `[skip log]` in the message so it doesn't trigger itself in a loop.

Want to run it locally without waiting for the Action (e.g. to preview the log before pushing)? Just run:
```bash
python scripts/update_log.py
```

---

---

## The portfolio site (`docs/index.html`)

A single-file, no-build static page that turns this repo into something you can link from a CV: your flight-path progress grid, live commit feed, certifications, and shipped projects — pulled straight from `.learning-progress.json` and the GitHub API, so it updates itself as you work.

**Setup (5 minutes):**
1. Open `docs/index.html` and edit the `CONFIG` object near the top of the `<script>` block — your name, tagline, email, LinkedIn, résumé link, `github.owner` / `github.repo`, your certifications, and your project list. Everything on the page is driven from that one object; you never touch the HTML/CSS.
2. Drop your actual `resume.pdf` into the `docs/` folder (or point `resumeUrl` at wherever it lives).
3. In your repo on GitHub: **Settings → Pages → Source** → deploy from branch `main`, folder `/docs` → Save.
4. Your site is live in a minute or two at `https://YOUR_USERNAME.github.io/YOUR_REPO_NAME/`. Put that link in your CV, LinkedIn, and email signature.

The page is plain HTML/CSS/JS — no build step, no npm install, works from any static host (Netlify, Vercel, or GitHub Pages all work identically if you'd rather use one of those instead).

**What it shows:**
- A 60-cell "flight path" grid — one cell per day, fills in automatically as `.learning-progress.json` records logged days, with today's cell highlighted.
- Live activity feed of your last 6 commits, pulled from the GitHub API in the visitor's browser (no server, no API key needed for public repos).
- Certifications with status pills (`earned` / `in-progress` / `planned`) — update the array as you actually pass exams.
- Project cards linking straight to each capstone's folder in this repo (and a live demo link, once you have one).

Before your first commit, or if `CONFIG.github.owner` is still a placeholder, the page shows honest empty/setup states instead of pretending there's data — no fake numbers.

---

## Suggested repo structure
```
your-repo/
├── README.md
├── ROADMAP.md
├── CERTIFICATIONS.md
├── LEARNING_LOG.md              # auto-updated, don't hand-edit
├── .learning-config.json        # auto-created on first run
├── .learning-progress.json      # auto-created, tracks streak/stats
├── .github/workflows/daily-log.yml
├── scripts/update_log.py
├── docs/
│   ├── index.html                # your CV portfolio site — see below
│   └── resume.pdf                # add your own
├── day01-numpy-basics/
├── day02-pandas-eda/
├── ...
└── day57-58-capstone/
```

## Portfolio tips for Day 59–60
- **Pin your best 4–6 repos** on your GitHub profile — not all 60. Quality over quantity.
- Every portfolio-piece README should read: problem → your approach → results (numbers/metrics) → link to a live demo if there is one.
- Deploy at least 2–3 demos publicly (Hugging Face Spaces is free and fast for this).
- Your capstone (`day57-58-capstone/`) should be the first thing linked from your GitHub profile README and your resume.
- If you want a Word/PDF version of your resume, or help drafting it from your capstone metrics, just ask — that's a five-minute follow-up once you're there.
