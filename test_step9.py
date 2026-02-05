from nlp.classifier import classify_contract

contract_text = """
EMPLOYMENT AGREEMENT

This Agreement is between the Employer and the Employee.
"""

print(classify_contract(contract_text))
