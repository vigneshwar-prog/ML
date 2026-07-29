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

## Git Publishing Workflow
- Remote repo: [https://github.com/vigneshwar-prog/ML](https://github.com/vigneshwar-prog/ML)
- After meaningful changes, commit and push to `main`.
- Suggested sequence:
  1. `git add -A`
  2. `git commit -m "<clear message>"`
  3. `git push origin main`
- Keep commits focused (one learning task or module per commit).

## Code File Convention
Every topic gets its own notebook inside a named subfolder under `code/`:

```
code/
  phase0/
    python_for_ml/
      numpy_basics.ipynb
      pandas_basics.ipynb
      matplotlib_basics.ipynb
    linear_algebra/
      vectors_matrices.ipynb
      dot_product.ipynb
    statistics/
      distributions.ipynb
      bias_variance.ipynb
    calculus/
      derivatives_gradients.ipynb
  phase1/
    linear_regression/
      theory_and_code.ipynb
    logistic_regression/
      theory_and_code.ipynb
  ...
```

Naming rules:
- Subfolder = topic name (e.g., `python_for_ml`, `linear_regression`)
- File = concept name, lowercase with underscores (e.g., `numpy_basics.ipynb`)
- Use one concept per notebook and split into section-wise cells
- Add a practice cell after each section for hands-on edits
- Save key plots with `plt.savefig()` when output files are needed
- Prefer notebook generation over `.py` for learning content

## Do NOT
- Skip theory and jump straight to code
- Use jargon without first defining it
- Add module summaries to plan.md (that file is the roadmap only)
- Create `.py` learning scripts by default when notebook format is requested
