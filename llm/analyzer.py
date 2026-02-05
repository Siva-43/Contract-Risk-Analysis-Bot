"""
LLM Analyzer (Free / Demo Mode)

This module simulates LLM-based legal reasoning.
Live LLM calls can be enabled by adding an API key.
"""

def explain_clause(clause_text: str) -> str:
    clause_lower = clause_text.lower()

    if "terminate" in clause_lower and "without cause" in clause_lower:
        return """
Plain-language explanation:
This clause allows the employer to end the agreement at any time without giving a reason.

Risk Level:
High

Why this is risky:
The clause is one-sided and gives full control to the employer. The employee has no protection.

Suggested safer alternative:
Either party may terminate this agreement by giving 30 days written notice, or termination may occur only for valid cause.
"""

    if "confidential" in clause_lower:
        return """
Plain-language explanation:
This clause requires the employee to keep company information private.

Risk Level:
Low

Why this is acceptable:
Confidentiality clauses are standard and protect business interests.

Suggested alternative:
No change required.
"""

    return """
Plain-language explanation:
This clause defines general contractual terms.

Risk Level:
Medium

Suggested improvement:
Clarify responsibilities, timelines, and mutual rights more explicitly.
"""
