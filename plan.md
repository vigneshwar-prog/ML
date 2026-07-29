# 🧠 Machine Learning & Deep Learning — Master Plan (Interview-Ready Edition)

> **Created:** 2026-07-29
> **Goal:** Learn ML/DL concepts deeply AND become interview-ready
> **Approach:** Theory → Code → Interview Training (one module at a time)
> **Tracking:** All learnings logged in `learning.html` — updated after every module

---

## 🎯 DUAL GOAL OF THIS PLAN

```
Goal 1 → UNDERSTAND concepts deeply (Theory + Code)
Goal 2 → ARTICULATE answers confidently (Interview Ready)
Goal 3 → TRACK every learning session in learning.html
```

---

## 📄 LEARNING TRACKER — learning.html

> **File Location:** `/Users/vigneshwar/ML/learning.html`
> **Purpose:** A visual, browser-based dashboard to track every module studied

### What gets logged after EVERY module:

| Field | Example |
|---|---|
| ✅ Module Name | Linear Regression |
| 📅 Date Studied | 2026-07-29 |
| 📖 Concepts Covered | MSE, Gradient Descent, Best-fit line |
| 💻 Code Written | Yes / No |
| 🎤 Interview Qs Practiced | 5 / 5 |
| 🧠 Recall Card | Filled |
| ⭐ Confidence Score | 1–5 stars |
| 📝 Personal Notes | "Remember — LR needs scaling for GD" |
| 🔁 Needs Revision | Yes / No |

### How to Use:
```
1. After finishing each module → open learning.html in browser
2. Click "Add Entry" → fill in the module details
3. Track your progress visually with phase completion bars
4. Use the revision flag to revisit weak topics before interviews
5. Export your notes before any mock interview session
```

### learning.html Features:
```
📊 Phase Progress Bars       → Visual % completion per phase
📅 Study Calendar            → Heatmap of study activity
🃏 Recall Cards View         → Quick-glance all 1-liners
🎤 Interview Q Bank          → All questions you've practiced
⚠️  Revision Flags           → Topics marked for re-study
📈 Confidence Tracker        → Star ratings per module over time
🔍 Search & Filter           → Find any concept instantly
🖨️  Print/Export             → Clean printable cheat sheet
```

---

```
┌─────────────────────────────────────────────┐
│  MODULE X.X — Algorithm Name                │
│                                             │
│  📖 Theory        → Concept explained       │
│  ⚙️  How It Works  → Step-by-step flow      │
│  📐 Math          → Key formula             │
│  💻 Code          → Python + sample data    │
│  🎤 Interview Q&A → Real questions + answers│
│  ⚠️  Trap Qs      → Trick questions         │
│  🧠 1-Liner       → Quick recall answer     │
└─────────────────────────────────────────────┘
```

---

## 🎤 INTERVIEW ANSWER FRAMEWORK (Use Every Time)

```
┌──────────────────────────────────────────────┐
│  ANSWER FRAMEWORK — "WHAT-WHY-HOW-WHEN"      │
│                                              │
│  WHAT  → Define the concept clearly          │
│  WHY   → Why it exists / what problem solved │
│  HOW   → How it works (intuition + formula)  │
│  WHEN  → When to use it vs alternatives      │
│  TRAP  → What can go wrong / limitations     │
└──────────────────────────────────────────────┘
```

---

## 📊 INTERVIEW QUESTION TYPES

```
Type 1 → Conceptual     "What is X? How does X work?"
Type 2 → Intuition      "Why do we use X over Y?"
Type 3 → Math           "What is the formula/loss function for X?"
Type 4 → Debugging      "What if model overfits/underfits?"
Type 5 → Scenario       "Given this situation, which algorithm?"
Type 6 → Code/Whiteboard "Write X from scratch"
Type 7 → Tricky/Edge    "What happens when...?"
```

---

## 📅 WEEKLY STUDY STRUCTURE (Per Module)

```
Day 1  → 📖 Theory          Read + understand the concept
Day 2  → ⚙️  How It Works    Diagrams, intuition, visualize
Day 3  → 💻 Code             Implement with sample dataset
Day 4  → 🧪 Experiment       Tweak params, observe changes
Day 5  → 🎤 Interview Drill  Answer 5–10 Qs out loud
Day 6  → 🔁 Mini Project     Apply the concept end-to-end
Day 7  → 😴 Rest + Revision  Review 1-liners and key formulas
```

---

## 🗺️ FULL ROADMAP

```
PHASE 0 → Prerequisites            (Week 1–2)
PHASE 1 → Classical ML             (Week 3–8)
PHASE 2 → Model Evaluation/Tuning  (Week 9–10)
PHASE 3 → Unsupervised Learning    (Week 11–12)
PHASE 4 → Deep Learning Foundations(Week 13–18)
PHASE 5 → Advanced Deep Learning   (Week 19–24)
PHASE 6 → Specialized Domains      (Week 25+)
PHASE 7 → Interview Bootcamp       (Week 25–28)
```

---

## 📌 PHASE 0 — Prerequisites (Week 1–2)

| Topic | What to Know | Interview Angle |
|---|---|---|
| **Python** | NumPy, Pandas, Matplotlib | "Walk me through data manipulation" |
| **Linear Algebra** | Vectors, Matrices, Dot Product | "Why do we use matrix multiplication in ML?" |
| **Statistics** | Mean, Variance, Distributions | "Explain bias-variance tradeoff" |
| **Calculus** | Derivatives, Chain Rule, Gradients | "How does gradient descent work?" |

### Progress Tracker
- [ ] Python (NumPy, Pandas, Matplotlib)
- [ ] Linear Algebra
- [ ] Statistics
- [ ] Calculus Basics

---

## 📚 PHASE 1 — Classical Machine Learning (Week 3–8)

### Progress Tracker
- [ ] Module 1.1 — Linear Regression
- [ ] Module 1.2 — Logistic Regression
- [ ] Module 1.3 — Decision Trees
- [ ] Module 1.4 — Random Forest
- [ ] Module 1.5 — Support Vector Machine (SVM)
- [ ] Module 1.6 — K-Nearest Neighbors (KNN)
- [ ] Module 1.7 — Naive Bayes
- [ ] Module 1.8 — Gradient Boosting (XGBoost, LightGBM)

---

### ✅ Module 1.1 — Linear Regression
> **Concept:** Predict a continuous value (e.g., house price)

**Theory:**
- Finds the best-fit line: `y = mx + b`
- Uses **Least Squares** to minimize error
- Loss function: **MSE (Mean Squared Error)**
- Learning via **Gradient Descent**

**How it works:**
```
Input(X) → Weighted sum → Predicted Y
         ↓
   Compare with actual Y
         ↓
   Calculate Error (MSE)
         ↓
   Update weights (Gradient Descent)
         ↓
   Repeat until error is minimized
```

**Key Formula:**
```
y = w₁x₁ + w₂x₂ + ... + b
MSE = (1/n) Σ(yᵢ - ŷᵢ)²
```

**Interview Questions:**
1. What is Linear Regression and when do you use it?
2. What is the difference between simple and multiple linear regression?
3. Does Linear Regression require feature scaling?
4. What are the assumptions of Linear Regression?
5. How do you detect multicollinearity?

**Trap Questions:**
- ⚠️ "Can Linear Regression be used for classification?" → (Technically yes but not ideal — use Logistic Regression)
- ⚠️ "What happens if features are correlated?" → (Multicollinearity — unstable coefficients)

**🧠 1-Liner:** *"Linear Regression finds the best-fit line by minimizing Mean Squared Error using Gradient Descent."*

---

### ✅ Module 1.2 — Logistic Regression
> **Concept:** Classify into 2 categories (e.g., spam or not spam)

**Theory:**
- Uses **Sigmoid function** to output probability (0 to 1)
- Loss function: **Binary Cross-Entropy**
- Decision boundary at 0.5

**Key Formula:**
```
σ(z) = 1 / (1 + e^(-z))
Loss = -[y·log(ŷ) + (1-y)·log(1-ŷ)]
```

**Interview Questions:**
1. Why can't we use MSE as the loss for Logistic Regression?
2. What is the sigmoid function and why is it used?
3. How do you handle multi-class classification with Logistic Regression?
4. What is the decision boundary?
5. Logistic Regression vs SVM — when to use which?

**Trap Questions:**
- ⚠️ "Is Logistic Regression a classification or regression algorithm?" → (Classification — despite the name!)
- ⚠️ "What if classes are not linearly separable?" → (Use kernel trick or switch to SVM/trees)

**🧠 1-Liner:** *"Logistic Regression uses the sigmoid function to squash output into a probability for binary classification."*

---

### ✅ Module 1.3 — Decision Trees
> **Concept:** Tree of if/else decisions to classify or predict

**Theory:**
- Splits data using **Gini Impurity** or **Information Gain (Entropy)**
- Prone to overfitting → solved by pruning or Random Forest

**Key Formula:**
```
Gini = 1 - Σ(pᵢ²)
Entropy = -Σ pᵢ · log₂(pᵢ)
Information Gain = Entropy(parent) - Weighted Avg Entropy(children)
```

**Interview Questions:**
1. How does a Decision Tree decide where to split?
2. What is Gini Impurity vs Entropy?
3. How do you prevent overfitting in a Decision Tree?
4. What is pruning?
5. Why are Decision Trees interpretable?

**Trap Questions:**
- ⚠️ "Do Decision Trees need feature scaling?" → (No — they are scale invariant)
- ⚠️ "Can a Decision Tree overfit?" → (Yes — deeply grown trees memorize training data)

**🧠 1-Liner:** *"Decision Trees recursively split data on the feature that gives the highest information gain."*

---

### ✅ Module 1.4 — Random Forest
> **Concept:** Ensemble of many decision trees using Bagging

**Theory:**
- Each tree trained on a random subset of data (**Bootstrap Aggregation / Bagging**)
- Random subset of features at each split
- Final answer = majority vote (classification) or average (regression)

**Interview Questions:**
1. How is Random Forest different from a single Decision Tree?
2. What is Bagging? How does it reduce variance?
3. What is the Out-of-Bag (OOB) error?
4. How does Random Forest handle missing values?
5. Random Forest vs Gradient Boosting — when to use which?

**Trap Questions:**
- ⚠️ "Does Random Forest overfit?" → (Much less than single trees, but can overfit with very noisy data)
- ⚠️ "Is Random Forest interpretable?" → (No — it's a black-box model)

**🧠 1-Liner:** *"Random Forest builds multiple decision trees on random data/feature subsets and aggregates their predictions to reduce variance."*

---

### ✅ Module 1.5 — Support Vector Machine (SVM)
> **Concept:** Find the best boundary (hyperplane) between classes

**Theory:**
- Maximizes the **margin** between classes
- **Support Vectors** — data points closest to the hyperplane
- Uses **kernel trick** for non-linear data (RBF, Polynomial)

**Interview Questions:**
1. What is a hyperplane and margin in SVM?
2. What are support vectors?
3. Explain the kernel trick with an example
4. When would you use RBF kernel vs linear kernel?
5. How does SVM handle outliers?

**Trap Questions:**
- ⚠️ "Does SVM work well with large datasets?" → (No — it's slow for large N; use SGD or neural nets)
- ⚠️ "Does SVM require feature scaling?" → (Yes — absolutely required)

**🧠 1-Liner:** *"SVM finds the optimal hyperplane that maximizes the margin between classes, using kernel trick for non-linear separation."*

---

### ✅ Module 1.6 — K-Nearest Neighbors (KNN)
> **Concept:** Classify based on K closest data points

**Theory:**
- No training phase — lazy learner
- Distance metric: **Euclidean Distance**
- Choose K wisely (too small = overfitting, too large = underfitting)

**Key Formula:**
```
Euclidean Distance = √(Σ(xᵢ - yᵢ)²)
```

**Interview Questions:**
1. How does KNN work? What is lazy learning?
2. How do you choose the value of K?
3. What distance metrics can be used?
4. What are the disadvantages of KNN?
5. Does KNN require feature scaling?

**Trap Questions:**
- ⚠️ "What is the time complexity of KNN prediction?" → (O(n·d) — slow for large datasets)
- ⚠️ "KNN for regression?" → (Yes — predict average of K nearest neighbors' values)

**🧠 1-Liner:** *"KNN classifies a point by majority vote of its K nearest neighbors using a distance metric — no training, all at prediction time."*

---

### ✅ Module 1.7 — Naive Bayes
> **Concept:** Probabilistic classifier using Bayes' Theorem

**Theory:**
- `P(Class|Features) ∝ P(Features|Class) × P(Class)`
- Assumes all features are **independent** (naive assumption)
- Great for text classification / NLP

**Key Formula:**
```
P(C|X) = P(X|C) · P(C) / P(X)
```

**Interview Questions:**
1. What is Bayes' Theorem?
2. What does "naive" mean in Naive Bayes?
3. When does the naive assumption break down?
4. Why is Naive Bayes good for text classification?
5. What is Laplace smoothing?

**Trap Questions:**
- ⚠️ "Can Naive Bayes handle correlated features?" → (Poorly — independence assumption breaks down)
- ⚠️ "What if a feature value never appeared in training?" → (Zero probability problem — solved by Laplace smoothing)

**🧠 1-Liner:** *"Naive Bayes uses Bayes' theorem with the naive assumption of feature independence to compute class probabilities."*

---

### ✅ Module 1.8 — Gradient Boosting (XGBoost / LightGBM)
> **Concept:** Ensemble that builds trees sequentially, each correcting previous errors

**Theory:**
- Builds trees one by one, each on the **residual errors** of the previous
- Uses **gradient descent** in function space
- XGBoost adds regularization; LightGBM is faster on large datasets

**Interview Questions:**
1. How is boosting different from bagging?
2. How does Gradient Boosting work step by step?
3. What is the learning rate in boosting?
4. XGBoost vs LightGBM vs CatBoost — differences?
5. How do you prevent overfitting in XGBoost?

**Trap Questions:**
- ⚠️ "Is boosting parallelizable?" → (Trees are sequential — but XGBoost parallelizes within each tree)
- ⚠️ "Does boosting reduce bias or variance?" → (Primarily bias — unlike bagging which reduces variance)

**🧠 1-Liner:** *"Gradient Boosting sequentially trains trees where each tree corrects the residual errors of the previous using gradient descent."*

---

## 📊 PHASE 2 — Model Evaluation & Tuning (Week 9–10)

### Progress Tracker
- [ ] Train/Val/Test Split
- [ ] Cross Validation (K-Fold)
- [ ] Confusion Matrix
- [ ] Precision, Recall, F1-Score
- [ ] ROC-AUC Curve
- [ ] Overfitting & Underfitting
- [ ] Regularization (L1, L2, ElasticNet)
- [ ] Hyperparameter Tuning
- [ ] Feature Engineering & Scaling

### Key Interview Questions

| Concept | Interview Question |
|---|---|
| Train/Val/Test Split | "Why not test on training data?" |
| Cross Validation | "What is K-Fold and why use it?" |
| Confusion Matrix | "Explain FP vs FN with a real example" |
| Precision & Recall | "When would you prefer recall over precision?" |
| ROC-AUC | "What does AUC = 0.5 mean?" |
| Overfitting | "How do you detect and fix overfitting?" |
| Regularization | "Difference between L1 and L2?" |
| Hyperparameter Tuning | "GridSearch vs RandomSearch — when to use which?" |
| Feature Scaling | "Why does SVM need scaling but trees don't?" |

---

## 🔍 PHASE 3 — Unsupervised Learning (Week 11–12)

### Progress Tracker
- [ ] K-Means Clustering
- [ ] DBSCAN
- [ ] PCA (Principal Component Analysis)
- [ ] t-SNE
- [ ] Autoencoders (intro)

| Algorithm | Key Interview Question |
|---|---|
| K-Means | "How do you choose K? What is the elbow method?" |
| DBSCAN | "How is DBSCAN different from K-Means?" |
| PCA | "What is PCA? When would you use it?" |
| t-SNE | "Can you use t-SNE for feature reduction in production?" |

---

## 🔥 PHASE 4 — Deep Learning Foundations (Week 13–18)

### Progress Tracker
- [ ] Artificial Neural Networks (ANN)
- [ ] Activation Functions
- [ ] Loss Functions
- [ ] Optimizers (SGD, Adam, RMSProp)
- [ ] Backpropagation
- [ ] Batch Normalization
- [ ] Dropout & Regularization
- [ ] CNN (Convolutional Neural Networks)
- [ ] RNN & LSTM
- [ ] Transformers & Attention Mechanism

| Module | Key Interview Questions |
|---|---|
| **ANN** | "What is backpropagation? Explain with math." |
| **Activation Fns** | "Why ReLU over Sigmoid in hidden layers?" |
| **Loss Functions** | "MSE vs Cross-Entropy — when to use which?" |
| **Optimizers** | "Difference between SGD, Adam, RMSProp?" |
| **Batch Norm** | "What is batch normalization and why use it?" |
| **Dropout** | "How does dropout prevent overfitting?" |
| **CNN** | "Explain convolution operation with an example" |
| **RNN/LSTM** | "What is vanishing gradient? How does LSTM solve it?" |
| **Transformers** | "Explain self-attention in simple terms" |

---

## 🚀 PHASE 5 — Advanced Deep Learning (Week 19–24)

### Progress Tracker
- [ ] Transfer Learning
- [ ] GANs (Generative Adversarial Networks)
- [ ] Object Detection (YOLO, Faster R-CNN)
- [ ] Word Embeddings (Word2Vec, GloVe)
- [ ] BERT & Fine-tuning
- [ ] Reinforcement Learning Basics

| Topic | Interview Angle |
|---|---|
| Transfer Learning | "When would you NOT use transfer learning?" |
| GANs | "What is mode collapse in GANs?" |
| Embeddings | "What are word embeddings? Word2Vec vs GloVe?" |
| Fine-tuning | "Explain how you would fine-tune BERT" |
| RL | "What is the explore-exploit tradeoff?" |

---

## 🎯 PHASE 6 — Specialized Domains (Week 25+)

Choose your path:

```
🖼️  Computer Vision     → OpenCV, YOLO, Diffusion Models
📝  NLP / LLMs          → HuggingFace, LangChain, Fine-tuning
📈  Time Series         → ARIMA, Prophet, Temporal Fusion
🤖  Reinforcement Lrn.  → OpenAI Gym, PPO, DQN
```

---

## 🏆 PHASE 7 — Interview Bootcamp (Week 25–28)

### Progress Tracker
- [ ] Classical ML Mock Interviews (50 Qs)
- [ ] Deep Learning Mock Interviews (50 Qs)
- [ ] Scenario & Case-Based Questions (30 Qs)
- [ ] Full Mock Interview Simulation

### 🔥 Interview Categories

#### 1️⃣ Conceptual Round
```
"Explain X like I'm a 5-year-old"
"What's the difference between X and Y?"
"Why does algorithm X fail when...?"
```

#### 2️⃣ Scenario / Case Round
```
"You have imbalanced data — what do you do?"
"Your model works in testing but fails in production — why?"
"Dataset has 80% missing values — how do you handle it?"
"Client wants 99% accuracy — how do you respond?"
```

#### 3️⃣ Math / Derivation Round
```
"Derive the gradient descent update rule"
"Why is log loss used in logistic regression?"
"Prove why L1 gives sparse weights"
```

#### 4️⃣ Code Round
```
"Implement linear regression from scratch"
"Code a confusion matrix without sklearn"
"Write K-Means clustering from scratch"
```

#### 5️⃣ ML System Design Round
```
"Design a recommendation system"
"How would you build a fraud detection model?"
"Design an ML pipeline for real-time predictions"
```

---

## 🛠️ TOOLS & LIBRARIES

```python
# Data
numpy, pandas

# Visualization
matplotlib, seaborn, plotly

# Classical ML
scikit-learn

# Deep Learning
tensorflow / keras
pytorch

# NLP
transformers (HuggingFace), nltk, spacy

# Experiment Tracking
mlflow, wandb
```

---

## 🧠 RECALL CARD TEMPLATE (Filled After Each Module)

```
┌─────────────────────────────────────────────┐
│  🃏 RECALL CARD — [Algorithm Name]          │
│                                             │
│  One-liner: "..."                           │
│  Formula:   ...                             │
│  Use when:  ...                             │
│  Fails when: ...                            │
│  Interview trap: "..."                      │
│  Answer: "..."                              │
└─────────────────────────────────────────────┘
```

---

## 📈 OVERALL PROGRESS

| Phase | Status | Completion |
|---|---|---|
| Phase 0 — Prerequisites | 🔲 Not Started | 0% |
| Phase 1 — Classical ML | 🔲 Not Started | 0% |
| Phase 2 — Evaluation & Tuning | 🔲 Not Started | 0% |
| Phase 3 — Unsupervised Learning | 🔲 Not Started | 0% |
| Phase 4 — Deep Learning | 🔲 Not Started | 0% |
| Phase 5 — Advanced DL | 🔲 Not Started | 0% |
| Phase 6 — Specialization | 🔲 Not Started | 0% |
| Phase 7 — Interview Bootcamp | 🔲 Not Started | 0% |

---

> 💡 **Next Step:** Say `"Start Module 1.1 — Linear Regression"` to begin your first session!
> Each session = Theory + Code + Interview Q&A + Recall Card 🎯
