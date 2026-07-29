# ML Learning Workspace — Agent Instructions

## Project Purpose
This is a personal **ML/DL self-study workspace** for a beginner learner targeting interview-readiness.
Not a software project. Do not suggest refactors, CI pipelines, or package structures.

## Key Files
- [plan.md](plan.md) — Full roadmap, phase breakdown, module content, and progress checklists
- [learning.html](learning.html) — Browser-based visual tracker; updated after every module session

## Learner Profile
- Beginner; always explain terms from first principles before writing code.
- Teach by doing — use small Python examples with real sample data.
- Ask interview-style questions mid-lesson to reinforce recall.

---

## Mandatory Module Format
Every module must follow this structure exactly:

```
📖 Theory        → Concept in plain English
⚙️  How It Works  → Step-by-step flow (diagram/pseudocode preferred)
📐 Math          → Key formula(s) only — no derivations unless asked
💻 Code          → Python snippet with sample data (NumPy/Pandas/sklearn)
🎤 Interview Q&A → 5 real questions with model answers
⚠️  Trap Qs      → 2–3 trick questions with why the common answer is wrong
🧠 1-Liner       → Single sentence quick-recall summary
```

## Interview Answer Framework (WHAT-WHY-HOW-WHEN-TRAP)
When answering any interview question:
- **WHAT** — Define the concept clearly
- **WHY** — What problem it solves / why it exists
- **HOW** — Intuition + formula
- **WHEN** — When to use it vs alternatives
- **TRAP** — Limitations or common misconceptions

## After Every Module
Update [learning.html](learning.html) with:
- Module name, date, concepts covered, code written (yes/no)
- Interview Qs practiced, recall 1-liner, confidence score (1–5), revision flag

---

## Phase Roadmap (from plan.md)
| Phase | Topic | Target Weeks |
|-------|-------|-------------|
| 0 | Prerequisites (Python, Linear Algebra, Stats, Calculus) | 1–2 |
| 1 | Classical ML (LR, Trees, SVM, KNN, NB, Boosting) | 3–8 |
| 2 | Model Evaluation & Tuning | 9–10 |
| 3 | Unsupervised Learning | 11–12 |
| 4 | Deep Learning Foundations | 13–18 |
| 5 | Advanced Deep Learning | 19–24 |
| 6 | Specialized Domains | 25+ |
| 7 | Interview Bootcamp | 25–28 |

## Environment Setup
- Virtual env: `.venv/` at workspace root (excluded from git via `.gitignore`)
- Activate: `source .venv/bin/activate`
- Install deps: `pip install -r requirements.txt`
- **After installing any new package**: run `pip freeze > requirements.txt` to keep it updated

Current packages (see [requirements.txt](requirements.txt)):
- Phase 0–1: `numpy`, `pandas`, `matplotlib`, `scikit-learn`
- Phase 4+ (add when needed): `torch`, `tensorflow`, `keras`

## Code File Convention
Every topic gets its own file inside a named subfolder under `code/`:

```
code/
  phase0/
    python_for_ml/
      numpy_basics.py
      pandas_basics.py
      matplotlib_basics.py
    linear_algebra/
      vectors_matrices.py
      dot_product.py
    statistics/
      distributions.py
      bias_variance.py
    calculus/
      derivatives_gradients.py
  phase1/
    linear_regression/
      theory_and_code.py
    logistic_regression/
      theory_and_code.py
  ...
```

Naming rules:
- Subfolder = topic name (e.g., `python_for_ml`, `linear_regression`)
- File = concept name, lowercase with underscores (e.g., `numpy_basics.py`)
- Include section headers (`SECTION 1`, `SECTION 2`, …) inside each file
- End each section with a `# ── PRACTICE: …` comment prompt
- Save plots with `plt.savefig()` alongside the script, not just `plt.show()`
- One concept per file — never combine unrelated topics

## Do NOT
- Skip theory and jump straight to code
- Use jargon without first defining it
- Add module summaries to plan.md (that file is the roadmap only)
- Create new Python files unless the user explicitly asks, or a module is being completed
