def assess_clause_risk(clause_text: str) -> dict:
    text = clause_text.lower()

    risk = "Low"
    reasons = []

    if "terminate" in text and "without cause" in text:
        risk = "High"
        reasons.append("Unilateral termination without cause")

    if "indemnify" in text or "penalty" in text:
        risk = "High"
        reasons.append("Financial liability or penalty clause")

    if "auto-renew" in text or "automatically renew" in text:
        risk = "Medium"
        reasons.append("Auto-renewal without explicit consent")

    if "arbitration" in text and "india" not in text:
        risk = "Medium"
        reasons.append("Arbitration outside India")

    if "confidential" in text:
        risk = max(risk, "Low")

    return {
        "risk_level": risk,
        "reasons": reasons
    }


def assess_contract_risk(clauses: list) -> dict:
    score_map = {"Low": 1, "Medium": 2, "High": 3}
    total_score = 0
    clause_results = []

    for clause in clauses:
        result = assess_clause_risk(clause)
        clause_results.append(result)
        total_score += score_map[result["risk_level"]]

    avg_score = total_score / len(clauses)

    if avg_score >= 2.5:
        overall = "High"
    elif avg_score >= 1.8:
        overall = "Medium"
    else:
        overall = "Low"

    return {
        "overall_risk": overall,
        "average_score": round(avg_score, 2),
        "clauses": clause_results
    }
