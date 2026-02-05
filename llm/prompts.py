EXPLAIN_CLAUSE_PROMPT = """
You are a legal assistant for Indian small and medium businesses.

Explain the following contract clause in very simple business language.
Avoid legal jargon.
Explain:
1. What this clause means
2. Why it may be risky (if applicable)
3. Who it favors (company or counterparty)

Clause:
\"\"\"
{clause}
\"\"\"
"""

RENEGOTIATION_PROMPT = """
You are a legal assistant helping an Indian SME renegotiate a contract.

Given the following clause and identified risk, suggest a safer alternative clause
that is more balanced and SME-friendly.

Clause:
\"\"\"
{clause}
\"\"\"

Identified Risk:
{risk_type}

Provide:
- A suggested alternative clause
- A one-line explanation of why it is safer
"""
