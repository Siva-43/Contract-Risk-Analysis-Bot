from llm.analyzer import explain_clause

clause = """
The Employer may terminate this Agreement at any time without cause by giving 30 days notice.
"""

print(explain_clause(clause))
