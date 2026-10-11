# RabTech Academy — AI & Machine Learning Internship

**Repository:** `RabTech-AI-ML-Internship`  
**Student:** Chandril Goswami  
**Program:** Artificial Intelligence & Machine Learning Internship  
**Platform:** RabTech Academy

## About This Repository

This repository contains my Artificial Intelligence and Machine Learning internship work, including problem framing, data quality assessment, preprocessing, model training and tuning, deep learning/NLP, and API deployment.

The objective is to develop a structured understanding of the end-to-end machine learning lifecycle, from understanding a business problem and validating data to evaluating models and preparing deployment artifacts.

## Project Structure

```text
RabTech-AI-ML-Internship/
├── 01_LinkedIn_Proof/
├── 02_Problem_Framing/
│   ├── 02_problem_framing.ipynb
│   ├── problem_framing_memo.md
│   ├── responsible_data_card.md
│   └── risk_register.csv
├── 03_Preprocessing/
│   └── 03_preprocessing_pipeline.ipynb
├── 04_Model_Tuning/
│   ├── 04_model_training_tuning.ipynb
│   └── model_comparison.csv
├── 05_Deep_Learning_NLP/
│   └── 05_text_classifier.ipynb
├── 06_FastAPI_Capstone/
│   ├── app/main.py
│   ├── tests/test_api.py
│   ├── requirements.txt
│   ├── Dockerfile
│   └── README.md
├── data/
│   └── customer-churn-training.csv
├── models/
├── reports/
├── .gitignore
├── requirements.txt
└── README.md
```

## Task 02 — Responsible Problem Framing

Task 02 focuses on framing a customer churn classification problem, inspecting the dataset, documenting data quality, identifying risks, and establishing a baseline model.

### Deliverables

- `02_problem_framing.ipynb` — exploratory inspection, validation, and baseline evaluation.
- `problem_framing_memo.md` — business problem, ML objective, evaluation approach, and limitations.
- `responsible_data_card.md` — dataset purpose, provenance, representation, quality, and responsible-use considerations.
- `risk_register.csv` — documented project risks and mitigation actions.

### Dataset Overview

- Dataset: Customer churn training data.
- Records: 12.
- Input features: 5, excluding the customer identifier and target.
- Target variable: `churned`.
- Task type: Binary classification.

### Baseline Evaluation

A majority-class baseline was established using Scikit-learn's `DummyClassifier` with `strategy="most_frequent"`.

| Metric | Result |
|---|---:|
| Accuracy | 0.6667 |
| Churn precision | 0.0000 |
| Churn recall | 0.0000 |
| Churn F1-score | 0.0000 |

**Interpretation:** The baseline predicted every test record as non-churn. It classified two non-churn records correctly but failed to identify the one churn record in the test set.

**Limitation:** The dataset contains only 12 records, with three records in the test set. These metrics are highly sensitive to individual predictions and do not establish reliable generalization or production readiness.

## Technology Stack

- Python
- Pandas and NumPy
- Scikit-learn
- Jupyter Notebook
- Git and GitHub
- FastAPI and Docker for the capstone work

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/Chandril6290Da/RabTech-AI-ML-Internship.git
cd RabTech-AI-ML-Internship
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Open the notebooks

```bash
jupyter notebook
```

Open the relevant notebook inside the corresponding task folder. Check the dataset path and required dependencies before running it.

## Responsible AI and Data Practices

This project emphasizes data quality, leakage prevention, transparent evaluation, responsible documentation, and awareness of limitations.

Dataset provenance, permitted use, and the official definition of the churn target should be verified before drawing business conclusions. No real customer decisions should be based on the current small-sample baseline.

## Project Status

- [x] Task 02 — Problem framing documentation and baseline evaluation
- [ ] Task 03 — Data preprocessing
- [ ] Task 04 — Model training and tuning
- [ ] Task 05 — Deep learning and NLP
- [ ] Task 06 — FastAPI capstone and deployment preparation

Task completion and approval remain subject to the internship's official requirements and review.

## Repository

[View this project on GitHub](https://github.com/Chandril6290Da/RabTech-AI-ML-Internship)

---

*Prepared as part of my AI & Machine Learning internship learning journey at RabTech Academy.*