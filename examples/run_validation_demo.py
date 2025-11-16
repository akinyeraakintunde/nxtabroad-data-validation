from nxtabroad_data_validation.validators import validate_applicant_sheet

if __name__ == "__main__":
    result = validate_applicant_sheet("examples/example_input.csv")

    if result.is_valid:
        print("✅ Sheet passed all validation checks.")
    else:
        print("❌ Issues found:")
        for issue in result.issues:
            loc = ""
            if issue.row_index is not None:
                loc += f" (row {issue.row_index})"
            if issue.column:
                loc += f" [column '{issue.column}']"
            print(f"- {issue.level}{loc}: {issue.message}")
