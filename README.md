# NxtAbroad Data Validation Toolkit

A lightweight Python toolkit used at **NxtAbroad Limited** to validate data involved in
visa and admission workflows (e.g. spreadsheets with applicant details, financial data,
and document checklists).

> Part of my Global Talent (Tech Nation) evidence for operational automation and
> contributions to the tech ecosystem.

---

## What It Does

- Validates **CSV/Excel** files used for visa/admissions processing.
- Checks for:
  - missing required columns and values
  - invalid formats (dates, email, currency)
  - numeric thresholds (e.g. minimum funds)
  - cross-field consistency (name, passport, date ranges)
- Generates human-readable **validation reports** for consultants.

---

## Usage

```python
from nxtabroad_data_validation.validators import validate_applicant_sheet

result = validate_applicant_sheet("data/applicants.csv")

if result.is_valid:
    print("Sheet passed all checks.")
else:
    print("Issues found:")
    for issue in result.issues:
        print(f"- {issue.level}: {issue.message}")
