from risk.risk_engine import assess_contract_risk

clauses = [
    "The Employer may terminate this Agreement without cause.",
    "The Employee shall maintain confidentiality.",
    "This agreement shall auto-renew annually."
]

result = assess_contract_risk(clauses)
print(result)
