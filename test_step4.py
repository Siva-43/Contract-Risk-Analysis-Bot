from nlp.text_extractor import extract_text
from nlp.clause_splitter import split_clauses
from risk.scorer import assess_clause_risk

text = extract_text("demo_contracts/sample.txt")
clauses = split_clauses(text)

for i, clause in enumerate(clauses, 1):
    risk = assess_clause_risk(clause)
    print(f"\nClause {i} Risk Level: {risk['risk_level']}")
    if risk["issues"]:
        for issue in risk["issues"]:
            print(f" - {issue['risk_type']} (trigger: {issue['keyword']})")
