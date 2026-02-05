from nlp.ner import extract_entities

contract_text = """
This Employment Agreement is entered into on 1 January 2024.

The Employer shall pay the Employee a salary of INR 500,000 per year.

This Agreement shall continue for 2 years.

This Agreement shall be governed by the laws of India.
"""

entities = extract_entities(contract_text)

print(entities)
