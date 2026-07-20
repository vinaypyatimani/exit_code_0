# 🗺️ 60-Day Roadmap: Mediocre Dev → AI Engineer

**Track:** Generative AI/LLM Engineering + Classical ML Engineering
**Pace:** 4+ hrs/day · **Starting point:** Strong software engineer, ~zero ML/AI background

Every day has: **Focus** (what/why) → **Learn** (docs/reading) → **Watch** (video, if useful) → **Book** (optional deep-dive) → **Build** (today's commit). Push the "Build" item to a folder named `dayNN-topic-slug/` in this repo, with a short `README.md` in that folder explaining what you built. That commit is what the auto-logger (see main `README.md`) picks up.

Don't aim for perfection — aim for a working, committed artifact every single day. A rough notebook that runs beats a perfect one that doesn't exist.

---

## Phase 0 — Foundations (Days 1–8)
*Goal: get fluent in the tools every ML/AI engineer uses daily, and build real intuition for the math, not just formulas.*

### Day 1 — Python for Data/ML + NumPy
**Focus:** Vectorized thinking. You already know Python; today is about thinking in arrays instead of loops.
**Learn:** [NumPy: the absolute basics](https://numpy.org/doc/stable/user/absolute_beginners.html) · [NumPy quickstart](https://numpy.org/doc/stable/user/quickstart.html)
**Book:** *Python Data Science Handbook* — Jake VanderPlas, Ch. 2 (free: [jakevdp.github.io/PythonDataScienceHandbook](https://jakevdp.github.io/PythonDataScienceHandbook/))
**Build:** `day01-numpy-basics/` — a notebook that loads a toy dataset as a NumPy array and implements (no loops): normalization, broadcasting-based feature scaling, and basic vectorized statistics. Benchmark against a naive `for`-loop version and record the speedup.

### Day 2 — Pandas for Data Wrangling
**Focus:** Real-world data is messy; pandas is how you clean it fast.
**Learn:** [10 minutes to pandas](https://pandas.pydata.org/docs/user_guide/10min.html) · [Kaggle: Pandas micro-course](https://www.kaggle.com/learn/pandas)
**Book:** *Python Data Science Handbook*, Ch. 3
**Build:** `day02-pandas-eda/` — pick a real CSV (Kaggle Titanic or similar), do cleaning, groupby aggregations, merges, and pivot tables. Save a cleaned output CSV + notebook.

### Day 3 — Data Visualization & EDA
**Focus:** You can't model what you haven't looked at.
**Learn:** [Matplotlib pyplot tutorial](https://matplotlib.org/stable/tutorials/pyplot.html) · [Seaborn tutorial](https://seaborn.pydata.org/tutorial.html)
**Build:** `day03-eda-visuals/` — full EDA notebook on the Day 2 dataset: distributions, correlations, outliers, 5+ charts, and a written "what I learned" section.

### Day 4 — Linear Algebra for ML
**Focus:** Vectors, matrices, dot products, eigenvectors — the language every ML model is written in.
**Watch:** 🎥 [3Blue1Brown — Essence of Linear Algebra](https://www.3blue1brown.com/topics/linear-algebra)
**Book:** *Mathematics for Machine Learning* — Deisenroth, Faisal, Ong, Ch. 2 (free: [mml-book.github.io](https://mml-book.github.io/))
**Build:** `day04-linalg-from-scratch/` — implement vector/matrix operations (dot product, matrix multiply, transpose, norm) in pure Python, then verify against NumPy.

### Day 5 — Calculus & Gradients
**Focus:** Derivatives and the chain rule are literally how neural nets learn.
**Watch:** 🎥 [3Blue1Brown — Essence of Calculus](https://www.3blue1brown.com/topics/calculus)
**Book:** *Mathematics for Machine Learning*, Ch. 5 (Vector Calculus)
**Build:** `day05-gradient-descent/` — implement gradient descent from scratch on a simple loss function, then on 1-variable linear regression. Plot the loss curve and the descent path.

### Day 6 — Probability & Statistics for ML
**Focus:** Every ML model is a statement about uncertainty.
**Watch:** 🎥 [StatQuest — Statistics Fundamentals playlist](https://www.youtube.com/@statquest/playlists)
**Book:** *Mathematics for Machine Learning*, Ch. 6 (Probability & Distributions)
**Build:** `day06-probability-lab/` — simulate common distributions, compute a Bayes' theorem example (e.g. medical test false-positive problem), and run a basic hypothesis test on a real dataset.

### Day 7 — Core ML Concepts
**Focus:** Bias/variance, train/test/validation split, overfitting, cross-validation — the vocabulary of the whole field.
**Learn:** [Google's Machine Learning Crash Course](https://developers.google.com/machine-learning/crash-course)
**Watch:** 🎥 [StatQuest — A Gentle Introduction to Machine Learning](https://www.youtube.com/watch?v=Gv9_4yMHFhI)
**Book:** *Hands-On Machine Learning with Scikit-Learn, Keras & TensorFlow* — Aurélien Géron, Ch. 1
**Build:** `day07-ml-concepts/` — a notebook demonstrating overfitting vs. underfitting on a toy dataset (polynomial degree sweep) plus `cross_val_score` in scikit-learn, with a short written explanation of bias/variance in your own words.

### Day 8 — Git Workflow, Project Structure & Week 1 Capstone
**Focus:** How real ML repos are organized, and locking in your auto-logging setup.
**Learn:** Git branching basics · [Cookiecutter Data Science structure](https://cookiecutter-data-science.drivendata.org/)
**Build:** `day08-week1-capstone/` — finish setting up this repo (see main `README.md` for the auto-logger), then do one polished, portfolio-quality EDA on a new dataset of your choice, pulling together everything from Days 1–7. Clean README, clean notebook, no dead code.

---

## Phase 1 — Classical ML Engineering (Days 9–20)
*Goal: understand the models that still power most production ML, and get fast at the full sklearn workflow.*

### Day 9 — Linear Regression
**Watch:** 🎥 [StatQuest — Linear Regression, Clearly Explained](https://www.youtube.com/@statquest)
**Learn:** [scikit-learn: LinearRegression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html)
**Book:** *Hands-On ML* (Géron), Ch. 4
**Build:** `day09-linear-regression/` — implement linear regression from scratch with gradient descent, then compare coefficients/RMSE against `sklearn.linear_model.LinearRegression` on a housing dataset.

### Day 10 — Logistic Regression & Classification Metrics
**Watch:** 🎥 StatQuest — Logistic Regression
**Book:** *Hands-On ML*, Ch. 3–4
**Build:** `day10-logistic-regression/` — binary classifier (e.g. churn or breast cancer dataset). Compute precision/recall/F1/ROC-AUC, plot confusion matrix and ROC curve, and write one paragraph on which metric matters most for this problem and why.

### Day 11 — Decision Trees
**Watch:** 🎥 StatQuest — Decision and Classification Trees
**Book:** *Hands-On ML*, Ch. 6
**Build:** `day11-decision-trees/` — train + visualize a tree, sweep `max_depth` and plot train vs. validation accuracy to see overfitting happen live.

### Day 12 — Random Forests & Bagging
**Watch:** 🎥 StatQuest — Random Forests
**Book:** *Hands-On ML*, Ch. 7
**Build:** `day12-random-forest/` — random forest on the same dataset, feature-importance bar chart, compare to the single tree from Day 11.

### Day 13 — Gradient Boosting (XGBoost/LightGBM)
**Watch:** 🎥 StatQuest — Gradient Boost series
**Learn:** [XGBoost docs](https://xgboost.readthedocs.io/) · [LightGBM docs](https://lightgbm.readthedocs.io/)
**Build:** `day13-gradient-boosting/` — train XGBoost and LightGBM on the same dataset, build a small comparison table (accuracy, training time) across all models so far.

### Day 14 — Support Vector Machines
**Watch:** 🎥 StatQuest — Support Vector Machines
**Book:** *Hands-On ML*, Ch. 5
**Build:** `day14-svm/` — SVM with linear/RBF/poly kernels on a 2D toy dataset, visualize the decision boundaries side by side.

### Day 15 — KNN & Naive Bayes
**Watch:** 🎥 StatQuest — Naive Bayes
**Build:** `day15-knn-naive-bayes/` — implement KNN from scratch (NumPy only) and compare to `sklearn`; build a Naive Bayes spam classifier on a text dataset.

### Day 16 — Clustering (K-Means, DBSCAN)
**Watch:** 🎥 StatQuest — K-means clustering
**Book:** *Hands-On ML*, Ch. 9
**Build:** `day16-clustering/` — customer-segmentation-style dataset, K-Means vs. DBSCAN, compare using silhouette score, visualize clusters.

### Day 17 — Dimensionality Reduction (PCA, t-SNE)
**Watch:** 🎥 StatQuest — PCA Main Ideas / t-SNE Clearly Explained
**Book:** *Hands-On ML*, Ch. 8
**Build:** `day17-dim-reduction/` — PCA + t-SNE on a high-dimensional dataset (e.g. MNIST digits), visualize in 2D, explain variance retained.

### Day 18 — Feature Engineering & Selection
**Learn:** [scikit-learn feature_selection](https://scikit-learn.org/stable/modules/feature_selection.html) · [category_encoders](https://contrib.scikit-learn.org/category_encoders/)
**Build:** `day18-feature-engineering/` — build a full `sklearn.Pipeline` with encoding, scaling, and mutual-information-based feature selection on a mixed categorical/numeric dataset.

### Day 19 — Model Evaluation & Hyperparameter Tuning
**Learn:** [GridSearchCV / RandomizedSearchCV](https://scikit-learn.org/stable/modules/grid_search.html) · [Optuna](https://optuna.org/)
**Build:** `day19-hyperparameter-tuning/` — tune a gradient boosting model with Optuna under proper nested cross-validation, log all trial results to a CSV.

### Day 20 — Classical ML Capstone (Portfolio Piece #1)
**Build:** `day20-classical-ml-capstone/` — a full Kaggle-style pipeline (data → EDA → feature engineering → model selection → tuning → evaluation → a `predict.py` script that loads the saved model). Polished README with a metrics table and what you'd try next with more time.

---

## Phase 2 — Deep Learning Foundations (Days 21–32)
*Goal: understand neural nets from first principles, then get fluent in PyTorch.*

### Day 21 — Neural Networks From Scratch
**Watch:** 🎥 [3Blue1Brown — But what is a neural network? (Deep Learning ch.1)](https://www.youtube.com/playlist?list=PLZZWrBYkx7Otcjr3eCLZDCgfpqnxMY29s)
**Book:** [Dive into Deep Learning](https://d2l.ai/), Ch. 3
**Build:** `day21-nn-from-scratch/` — implement a single-layer perceptron in raw NumPy, train it on a toy binary classification problem.

### Day 22 — Backpropagation From Scratch
**Watch:** 🎥 [Andrej Karpathy — micrograd: building an autograd engine](https://www.youtube.com/watch?v=VMj-3S1tku0) (video 1 of [Neural Networks: Zero to Hero](https://www.youtube.com/playlist?list=PLAqhIrjkxbuWI23v9cThsA9GvCAUhRvKZ))
**Build:** `day22-micrograd/` — follow along and build your own tiny autograd engine, then train a small MLP with it.

### Day 23 — PyTorch Basics
**Learn:** [PyTorch: Learn the Basics](https://pytorch.org/tutorials/beginner/basics/intro.html)
**Watch:** 🎥 [PyTorch for Deep Learning & Machine Learning — Full Course](https://www.youtube.com/watch?v=V_xro1bcAuA) (Daniel Bourke, freeCodeCamp — watch the first ~2 hrs today)
**Build:** `day23-pytorch-basics/` — notebook covering tensors, autograd, and a minimal training loop on synthetic data.

### Day 24 — MLP in PyTorch (MNIST)
**Build:** `day24-mlp-mnist/` — train an MLP image classifier on MNIST or FashionMNIST, plot loss/accuracy curves.

### Day 25 — Optimizers & Regularization
**Learn:** [PyTorch optim docs](https://pytorch.org/docs/stable/optim.html)
**Book:** *Deep Learning* — Goodfellow, Bengio, Courville (free: [deeplearningbook.org](https://www.deeplearningbook.org/)), Ch. 7–8
**Build:** `day25-regularization-ablation/` — take the Day 24 MLP and run an ablation: with/without dropout, batchnorm, weight decay. Compare curves in one plot.

### Day 26 — CNN Fundamentals
**Watch:** 🎥 StatQuest — Convolutional Neural Networks
**Book:** [Dive into Deep Learning](https://d2l.ai/), Ch. 7
**Build:** `day26-conv-from-scratch/` — implement 2D convolution and max-pooling manually in NumPy on a sample image (no training yet) to build real intuition.

### Day 27 — CNNs in PyTorch
**Build:** `day27-cnn-cifar10/` — train a small CNN on CIFAR-10, log accuracy, and plot a grid of misclassified examples.

### Day 28 — Transfer Learning
**Learn:** [PyTorch transfer learning tutorial](https://pytorch.org/tutorials/beginner/transfer_learning_tutorial.html)
**Build:** `day28-transfer-learning/` — fine-tune a pretrained ResNet/EfficientNet on a small custom image dataset, write a simple inference script.

### Day 29 — RNN / LSTM Fundamentals
**Watch:** 🎥 StatQuest — Long Short-Term Memory (LSTM)
**Book:** [Dive into Deep Learning](https://d2l.ai/), Ch. 9
**Build:** `day29-char-rnn/` — a character-level RNN that generates text (names, or a small text corpus).

### Day 30 — Sequence Modeling Project
**Build:** `day30-sequence-project/` — time-series forecasting OR sentiment classification with an LSTM, benchmarked against a naive baseline (moving average / bag-of-words).

### Day 31 — Training at Scale: Experiment Tracking
**Learn:** [Weights & Biases quickstart](https://docs.wandb.ai/quickstart) · [PyTorch AMP (mixed precision)](https://pytorch.org/docs/stable/amp.html)
**Build:** `day31-experiment-tracking/` — re-run one earlier training job with W&B logging and mixed precision, compare speed/memory before and after.

### Day 32 — Deep Learning Capstone (Portfolio Piece #2)
**Build:** `day32-cv-capstone/` — an image classifier of your choice, wrapped in a small [Gradio](https://www.gradio.app/) demo deployed to [Hugging Face Spaces](https://huggingface.co/spaces).

---

## Phase 3 — NLP & Transformers (Days 33–42)
*Goal: understand exactly how attention and transformers work — the single highest-leverage thing to actually know deeply for an AI engineer.*

### Day 33 — Text Preprocessing & Word Embeddings
**Learn:** [gensim word2vec tutorial](https://radimrehurek.com/gensim/models/word2vec.html)
**Book:** *Speech and Language Processing* — Jurafsky & Martin (free draft: [web.stanford.edu/~jurafsky/slp3](https://web.stanford.edu/~jurafsky/slp3/)), Ch. 6
**Build:** `day33-word-embeddings/` — train word2vec on a small corpus, visualize embeddings with t-SNE, inspect nearest neighbors of a few words.

### Day 34 — The Attention Mechanism
**Watch:** 🎥 [3Blue1Brown — Attention in transformers, visually explained](https://www.youtube.com/playlist?list=PLZZWrBYkx7Otcjr3eCLZDCgfpqnxMY29s)
**Book:** [Dive into Deep Learning](https://d2l.ai/), Ch. 11
**Build:** `day34-attention-from-scratch/` — implement scaled dot-product attention (and multi-head) from scratch in PyTorch on toy sequences.

### Day 35–36 — Build a Mini-GPT From Scratch (2 days)
**Watch:** 🎥 [Andrej Karpathy — Let's build GPT: from scratch, in code, spelled out](https://www.youtube.com/playlist?list=PLAqhIrjkxbuWI23v9cThsA9GvCAUhRvKZ)
**Reference:** [github.com/karpathy/nanoGPT](https://github.com/karpathy/nanoGPT)
**Build:** `day35-36-nanogpt/` — follow along and build a character-level GPT, train it on a small text corpus (e.g. Shakespeare), generate samples. This is the single most important exercise in the whole roadmap for actually understanding LLMs — don't rush it.

### Day 37 — The Hugging Face Ecosystem
**Learn:** [Hugging Face LLM Course, Ch. 1–4](https://huggingface.co/learn/llm-course/en/chapter1/1)
**Build:** `day37-huggingface-pipelines/` — use `transformers` pipelines for classification, NER, and summarization on real text; note what each model gets right/wrong.

### Day 38 — Fine-tune BERT for Classification
**Build:** `day38-finetune-bert/` — fine-tune DistilBERT on a text classification dataset (e.g. IMDB or tweet sentiment), push the model to the Hugging Face Hub.

### Day 39 — Fine-tune for NER / QA
**Build:** `day39-finetune-ner-qa/` — fine-tune a token-classification or question-answering model, evaluate with `seqeval` or SQuAD-style metrics.

### Day 40 — How LLMs Are Actually Trained
**Watch:** 🎥 [Andrej Karpathy — Deep Dive into LLMs like ChatGPT](https://www.youtube.com/watch?v=7xTGNNLPyMI) (long — watch pretraining + post-training sections today, finish tomorrow if needed)
**Build:** `day40-llm-training-notes/` — a written summary (your own words) of pretraining → SFT → RLHF, plus a small script that shows the difference in output between a base-style prompt and an instruction-style prompt on an open model.

### Day 41 — NLP Evaluation & Benchmarks
**Learn:** [Hugging Face `evaluate` library](https://huggingface.co/docs/evaluate) · GLUE/SuperGLUE benchmarks
**Build:** `day41-model-evaluation/` — properly evaluate your Day 38/39 models (F1, EM, ROUGE as relevant), write a short model card documenting strengths/limitations.

### Day 42 — NLP Capstone (Portfolio Piece #3)
**Build:** `day42-nlp-capstone/` — polish and publish a fine-tuned model with a live Gradio demo on Hugging Face Spaces. Write a proper model card.

---

## Phase 4 — Generative AI / LLM Engineering (Days 43–56)
*Goal: the actual "AI engineer" job — building applications on top of foundation models. This is where portfolio pieces get the most attention from hiring managers.*

### Day 43 — Prompt Engineering Fundamentals
**Learn:** [DeepLearning.AI — ChatGPT Prompt Engineering for Developers](https://www.deeplearning.ai/short-courses/chatgpt-prompt-engineering-for-developers/) (free, ~1.5 hrs)
**Book:** *Prompt Engineering for Generative AI* — James Phoenix & Mike Taylor, Ch. 1–3
**Build:** `day43-prompt-patterns/` — build a small library of prompt patterns (zero-shot, few-shot, chain-of-thought) tested against a fixed set of tasks; log and compare outputs.

### Day 44 — Advanced Prompting (CoT, ReAct, structured output)
**Learn:** [promptingguide.ai](https://www.promptingguide.ai/)
**Build:** `day44-react-from-scratch/` — implement a ReAct-style reasoning + tool-use loop **by hand** (no framework) against an LLM API, so you understand what frameworks are automating before you use them.

### Day 45 — Working With LLM APIs
**Learn:** [docs.claude.com](https://docs.claude.com) (Anthropic API docs) and/or the OpenAI platform docs — check current docs since APIs evolve fast
**Build:** `day45-llm-api-app/` — a small CLI or web app wrapping an LLM API: streaming responses, system prompts, multi-turn conversation memory.

### Day 46 — Structured Outputs & Function/Tool Calling
**Build:** `day46-function-calling/` — an "assistant with tools" (calculator, mock weather lookup, etc.) using JSON-schema function calling, validated with Pydantic.

### Day 47 — Intro to RAG: Embeddings & Vector Search
**Watch:** 🎥 [Learn RAG From Scratch — LangChain Engineer](https://www.youtube.com/watch?v=sVcwVQRHIc8)
**Build:** `day47-rag-from-scratch/` — generate embeddings for a small document set (`sentence-transformers`) and implement cosine-similarity search yourself, no vector DB yet.

### Day 48 — Vector Databases
**Learn:** [Chroma docs](https://docs.trychroma.com/) · [FAISS](https://github.com/facebookresearch/faiss)
**Build:** `day48-vector-db/` — swap Day 47's manual search for a real vector DB (Chroma or FAISS), benchmark retrieval speed as the corpus grows.

### Day 49 — End-to-End RAG Pipeline
**Build:** `day49-rag-pipeline/` — a full RAG chatbot over a real document set (your resume + notes, or a PDF corpus) that cites its sources in the answer.

### Day 50 — LangChain
**Learn:** [python.langchain.com](https://python.langchain.com/)
**Watch:** 🎥 [DeepLearning.AI — LangChain for LLM Application Development](https://www.deeplearning.ai/short-courses/langchain-for-llm-application-development/) (Harrison Chase + Andrew Ng, free)
**Build:** `day50-langchain-rag/` — rebuild Day 49's RAG pipeline using LangChain's chains/retrievers/memory abstractions.

### Day 51 — LlamaIndex
**Learn:** [docs.llamaindex.ai](https://docs.llamaindex.ai/)
**Build:** `day51-llamaindex-rag/` — rebuild the same RAG pipeline with LlamaIndex; write a short comparison note (LangChain vs. LlamaIndex DX) in the README.

### Day 52 — AI Agents Fundamentals
**Learn:** [Hugging Face AI Agents Course](https://huggingface.co/learn/agents-course)
**Build:** `day52-single-tool-agent/` — a single-tool ReAct agent using a framework (LangChain agents, or your own loop refined from Day 44).

### Day 53 — Multi-Tool Agents With LangGraph
**Watch:** 🎥 [LangGraph Complete Course for Beginners](https://www.youtube.com/watch?v=jGg_1h0qzaM)
**Build:** `day53-langgraph-agent/` — a multi-tool agent (web search + calculator + your Day 48 retriever) with LangGraph, including basic state/memory.

### Day 54 — Fine-tuning LLMs (LoRA / QLoRA / PEFT)
**Learn:** [Hugging Face PEFT docs](https://huggingface.co/docs/peft)
**Book:** *LLM Engineer's Handbook* — Iusztin & Labonne, fine-tuning chapters
**Build:** `day54-lora-finetune/` — LoRA fine-tune a small open model (1–3B params) on a custom instruction dataset using a free Colab GPU, push the adapter to the Hugging Face Hub.

### Day 55 — LLM Evaluation & Guardrails
**Learn:** [RAGAS docs](https://docs.ragas.io/)
**Build:** `day55-rag-evaluation/` — build an eval harness for your Day 49/53 app (faithfulness, answer relevance, basic hallucination checks) and add simple input/output guardrails.

### Day 56 — LLMOps: Deployment, Monitoring, Cost
**Learn:** [FastAPI docs](https://fastapi.tiangolo.com/) · Docker basics
**Build:** `day56-llmops-deploy/` — wrap your RAG/agent app in a FastAPI service, containerize with Docker, add token-usage/cost logging, deploy to a free host (Render, Fly.io, or Hugging Face Spaces).

---

## Phase 5 — Capstone & Portfolio (Days 57–60)
*Goal: turn 56 days of practice into the two or three artifacts a hiring manager will actually look at.*

### Day 57–58 — Full Capstone Project (2 days) — Flagship Portfolio Piece
**Build:** `day57-58-capstone/` — a production-shaped GenAI application combining RAG + an agent with tools + a simple UI, publicly deployed, with basic tests and an architecture diagram in the README. Pick something you'd actually use — that authenticity shows in interviews.

### Day 59 — Portfolio Polish
**Task:** Clean up every repo from the last 58 days. Write strong READMEs (problem → approach → results → demo link/gif) for your 4–6 best pieces, pin them on your GitHub profile, and write a GitHub profile README. Deploy any demos that are still local-only.

### Day 60 — Resume, LinkedIn & What's Next
**Task:** Rewrite resume bullets using concrete capstone metrics. Update LinkedIn with your new projects and skills. Pick 1–2 items from `CERTIFICATIONS.md` to schedule next. Write yourself a 30/60/90-day post-program plan (e.g. deeper MLOps, a specific domain, or a harder cloud certification).

---

## How to use the "Build" links
Each day's project should live in its own folder, e.g.:
```
day09-linear-regression/
├── README.md          # what you built, what you learned, one chart if relevant
├── notebook.ipynb      (or .py scripts)
└── requirements.txt    # only if it diverges from the repo-wide one
```
Commit and push at the end of each day (or whenever you finish) — the auto-logger in `README.md` picks up your commit automatically and updates `LEARNING_LOG.md`.
