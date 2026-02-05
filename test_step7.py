from nlp.clause_splitter import split_clauses

contract_text = """
EMPLOYMENT AGREEMENT

1. TERM
This Agreement shall commence on 1 January 2024 and continue for two years.

2. TERMINATION
The Employer may terminate this Agreement without cause by giving 30 days notice.

3. CONFIDENTIALITY
The Employee shall not disclose confidential information during or after employment.

4. GOVERNING LAW
This Agreement shall be governed by the laws of India.
"""

clauses = split_clauses(contract_text)

for i, clause in enumerate(clauses, 1):
    print(f"\n--- Clause {i} ---")
    print(clause)
