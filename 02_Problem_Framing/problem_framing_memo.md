# ML Problem Framing Memo
## Customer Churn Prediction

**Project:** RabTech Academy — Artificial Intelligence & Machine Learning Internship  
**Task:** ML Problem Framing & Responsible Data Card  
**Status:** Initial Analysis Completed; Baseline Evaluation Pending  
**Review Date:** 11 October 2026

---

## 1. Problem Statement

Customer churn occurs when a customer stops using a company's service. Identifying customers who may discontinue a service could help an organisation improve customer satisfaction and plan retention activities.

The objective of this project is to investigate whether machine learning can predict customer churn using historical customer information.

The supplied dataset contains 12 records and 7 columns. Initial inspection identified five candidate predictive features, one customer identifier, and one target column.

## 2. Business Objective

The proposed business objective is to support a customer-retention team in identifying customers who may be at risk of leaving.

Potential actions include reviewing customer concerns, improving service quality, and offering appropriate support.

The model will provide decision-support information only. It will not independently terminate accounts, deny services, or make decisions that materially disadvantage customers.

## 3. ML Problem Definition

**Problem type:** Supervised binary classification.

**Target variable:** `churned`

**Observed target values:**
- `0`: Non-churn
- `1`: Churn

The exact target definition, label-generation method, and observation period must be confirmed with the dataset provider.

**Unit of observation:** One customer record, subject to confirmation that each row represents a distinct customer at a defined observation time.

**Candidate features:**
- `tenure_months`
- `support_tickets`
- `monthly_spend_inr`
- `last_login_days`
- `plan_type`

The `customer_id` column will be excluded from model inputs because it serves as an identifier rather than an intended behavioural predictor.

## 4. Prediction Timing and Action Window

The intended prediction point is a defined date when the customer is still eligible for retention outreach.

The action window is the future period during which churn is to be predicted. Its duration has not yet been established because the dataset documentation does not currently specify the prediction horizon.

Before modeling, the target-generation process and the timing of each feature must be verified. Features containing information recorded after the prediction point must not be used.

## 5. Dataset Assessment

Initial dataset inspection produced the following results:

| Assessment | Result |
|---|---|
| Records | 12 |
| Columns | 7 |
| Missing values | 0 |
| Duplicate rows | 0 |
| Duplicate customer IDs | 0 |
| Invalid observed churn labels | 0 |
| IQR-flagged numerical outliers | 0 |
| Non-churn records | 7 (58.33%) |
| Churn records | 5 (41.67%) |

No missing values, duplicate records, invalid observed binary labels, or IQR-flagged numerical outliers were detected in the initial checks.

These results do not guarantee that every value is accurate or that the dataset represents the broader customer population.

## 6. Is Machine Learning Justified?

Machine learning is a reasonable method to investigate because the target is binary and multiple customer attributes are available as candidate predictors.

However, the current dataset contains only 12 records. This is insufficient to establish reliable generalisation, robust model comparisons, calibration, or fairness across customer groups.

Therefore, the current work should be treated as an educational baseline experiment, not as a production-ready churn prediction system.

A larger, representative, appropriately licensed dataset will be required before considering real-world deployment.

## 7. Non-ML Baseline

The first baseline will use a `DummyClassifier` that predicts the majority class from the training data.

This baseline will establish a minimum reference point for model evaluation.

A Logistic Regression classifier may be evaluated as a simple learned baseline if the data split permits meaningful evaluation.

An existing retention policy may also be compared if suitable historical outcomes are available.

## 8. Evaluation Strategy

The evaluation plan will include:

- Confusion matrix
- Precision
- Recall
- F1-score
- Balanced accuracy
- ROC-AUC and PR-AUC where estimable

False-positive and false-negative counts will be interpreted in the context of customer-retention costs.

False positives may lead to unnecessary retention outreach. False negatives may cause potentially at-risk customers to be missed.

The data will be split before fitting learned preprocessing transformations. The final test data will remain separate from model selection.

Given the very small sample size, all performance estimates will be reported with explicit limitations. A single test split will not be treated as evidence of reliable production performance.

## 9. Risks and Mitigation

**Data leakage:** Verify feature timing and exclude information unavailable at prediction time.

**Privacy:** Verify permitted use, minimise unnecessary personal information, and avoid publishing customer-level data without authorisation.

**Sampling bias:** Document unknown sampling methods and avoid generalising beyond the observed records.

**Class imbalance:** Report class distribution and use class-aware evaluation metrics.

**False predictions:** Keep predictions under human review and do not treat them as certain outcomes.

**Performance deterioration:** Require monitoring and a manual fallback before any future deployment.

## 10. Responsible Use and Deployment Gate

The model must not be used for automated account termination, service denial, or other unsupported high-impact decisions.

Before deployment can be considered, the project must establish:

1. Verified data provenance and usage permission.
2. A clearly defined churn target and prediction horizon.
3. Leakage-free preprocessing and evaluation.
4. Adequate representative data.
5. Acceptable validation performance and probability calibration, where appropriate.
6. Privacy, fairness, human-review, monitoring, and rollback safeguards.

If these conditions cannot be met, the project will remain an educational analysis and the organisation should use an appropriate manual process.

## 11. Current Conclusion

The initial inspection indicates that the dataset is structurally usable for a small educational experiment: all 12 records have complete observed values, customer IDs are unique, and both target classes are present.

However, the dataset is too small to support strong conclusions about predictive performance or real-world applicability.

The next step is to implement a majority-class baseline, establish a careful evaluation strategy, and document the limitations before considering more complex models.

---

**Final status:** Problem framed; baseline evaluation and provenance verification pending.


## Baseline Model Evaluation

### Baseline approach
A majority-class baseline was established using Scikit-learn's `DummyClassifier` with `strategy="most_frequent"`. The target variable was `churned`, and `customer_id` was excluded from the input features.

### Experimental setup
- Total records: 12
- Training records: 9
- Testing records: 3
- Train-test split: 75:25
- Random state: 42
- Stratification: Enabled

### Results
- Accuracy: 0.6667
- Churn precision: 0.0000
- Churn recall: 0.0000
- Churn F1-score: 0.0000

The baseline predicted every test record as non-churn. It correctly classified two non-churn records but failed to identify the single churn record in the test set.

### Interpretation and limitations
Although the baseline achieved 66.67% accuracy, it failed to detect any churn cases. Therefore, accuracy alone is insufficient for evaluating this classification problem. Recall, precision, F1-score, and the confusion matrix should also be considered.

The dataset contains only 12 records, with just three records in the test set. Consequently, these evaluation metrics are highly sensitive to individual predictions and cannot establish reliable generalization or production readiness.

### Next steps
Obtain a substantially larger, representative dataset; confirm the official definition and observation period of the churn target; verify data provenance and permitted use; and compare the baseline with a preprocessing pipeline and suitable classification models using leakage-safe validation. Report uncertainty and avoid making real customer decisions from this small sample.