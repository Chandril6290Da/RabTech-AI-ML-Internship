# Responsible Data Card — Customer Churn Prediction

## 1. Dataset Purpose

**Objective:** Evaluate whether machine learning can help identify customers who may discontinue a service.

**Intended decision:** Support human-reviewed customer retention outreach and service improvement.

**Prohibited uses:** The model must not independently terminate accounts, deny services, or make unsupported high-impact decisions.

**Non-ML baseline:** Majority-class prediction and, where available, an existing retention policy.

**Prediction target:** `churned`, subject to verification of the provider's target definition.

## 2. Provenance and Permission

**Dataset:** Customer Churn Training Dataset supplied through RabTech Academy's starter-files link.

**Collection method:** Unknown; requires confirmation from the dataset provider.

**License and permitted use:** Not yet verified. Confirm whether public repository publication and redistribution are permitted.

**Consent and privacy:** Consent status and the presence of personal or identifying information require verification.

**Data handling:** Avoid publishing unnecessary customer-level records. Review the dataset and repository contents before making them public.

## 3. Population and Representation

**Dataset size:** 12 rows and 7 columns.

**Represented population:** Exact population and sampling method are unknown.

**Known limitations:** The dataset is very small and may not represent the broader customer population.

**Target distribution:**
- Non-churn (`0`): 7 records (58.33%)
- Churn (`1`): 5 records (41.67%)

**Interpretation:** Both classes are represented. However, the small sample is insufficient to establish reliable population-level performance or fairness.

## 4. Features and Target

**Target:** `churned` — binary label with observed values `0` and `1`. The precise business definition and observation period must be confirmed.

**Candidate features:**
- `tenure_months`: customer tenure in months
- `support_tickets`: number of support tickets
- `monthly_spend_inr`: monthly spending in INR
- `last_login_days`: reported last-login age in days
- `plan_type`: subscription plan category

**Identifier:** `customer_id` uniquely identifies all 12 observed records and is excluded from the candidate model inputs.

**Potential leakage:** Verify that every feature was available at the intended prediction time. Confirm the reference date for `last_login_days` and check whether any feature incorporates post-churn information.

**Sensitive attributes and proxies:** No sensitive attributes have been established from the initial column inspection. Further provenance and feature review is required to assess potential proxies.

## 5. Quality Checks

| Check | Observed result |
|---|---|
| Dataset dimensions | 12 rows, 7 columns |
| Missing values | 0 in all columns |
| Duplicate rows | 0 |
| Duplicate customer IDs | 0 |
| Negative tenure | 0 |
| Negative support tickets | 0 |
| Non-positive monthly spend | 0 |
| Negative last-login days | 0 |
| Invalid binary target values | 0 |
| IQR-flagged numerical outliers | 0 |
| Unique customer IDs | Yes |
| Plan categories observed | Basic, Pro, Standard |

**Quality limitations:** The checks above do not establish that every value is accurate, plausible, or correctly defined. Outlier detection with 12 records has limited power.

**Train/test separation:** Not yet completed at the time of this inspection. Split the data before fitting learned preprocessing transformations.

**Data validation status:** Initial checks completed; provenance, business validity, target definition, and leakage review remain outstanding.

## 6. Risks and Safeguards

| Risk | Potential impact | Mitigation |
|---|---|---|
| Small sample size | Unstable estimates and unreliable generalisation | Obtain more representative data and report uncertainty |
| Data leakage | Inflated evaluation scores | Audit feature timing and isolate the test set |
| False positives | Unnecessary retention outreach | Measure precision and choose thresholds using business costs |
| False negatives | Customers at risk may be missed | Measure recall and review missed cases |
| Privacy exposure | Customer information may be disclosed | Verify permissions, minimise data and restrict access |
| Unrepresentative data | Unequal or poor performance on other populations | Verify sampling and evaluate appropriate subgroups when permitted |
| Model drift | Performance may deteriorate | Monitor data quality and outcomes over time |
| Misuse | Predictions may be treated as certain or used inappropriately | Require human review and document intended use |

**Human oversight:** Predictions are decision-support signals, not definitive statements about individual customers.

**Abstention and fallback:** Define a review process for invalid inputs and uncertain predictions. If the model or data validation fails, use an approved manual process.

**Rollback:** Suspend model-assisted decisions if serious data-quality failures or unacceptable performance deterioration are detected.

## 7. Intended Evaluation

**Baselines:**
- Majority-class `DummyClassifier`
- Logistic Regression
- Existing retention policy, if measurable and available

**Performance metrics:**
- Precision
- Recall
- F1-score
- Confusion matrix
- Balanced accuracy
- ROC-AUC and PR-AUC, where estimable

**Calibration:** Evaluate probability calibration only when sufficient independent evaluation data is available.

**Fairness:** Assess relevant group-level performance only where lawful, justified data and adequate sample sizes are available.

**Error analysis:** Inspect false positives, false negatives, data-quality issues, and potential leakage.

**Model selection:** Select using validation data and documented business costs. Keep the final test set separate until final evaluation.

**Deployment gate:** Do not recommend production deployment based on this 12-row dataset alone. Obtain suitable data, validate performance, and review privacy, fairness, and operational safeguards first.

## 8. Review Status

**Current status:** Initial data-quality inspection completed; modeling and final evaluation pending.

**Outstanding items:**
1. Verify dataset provenance, permission, and target definition.
2. Review feature timing and leakage risks.
3. Establish a reproducible train/test strategy.
4. Evaluate a baseline and document uncertainty.
5. Complete final risk and intended-use review.

**Review date:** 11 October 2026

**Project:** RabTech Academy — AI & Machine Learning Internship