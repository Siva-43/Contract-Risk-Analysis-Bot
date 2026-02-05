def calculate_risk_score(risks):
    score = 0

    for r in risks:
        if r["severity"] == "High":
            score += 40
        elif r["severity"] == "Medium":
            score += 25
        elif r["severity"] == "Low":
            score += 10

    if score >= 70:
        level = "High"
    elif score >= 40:
        level = "Medium"
    else:
        level = "Low"

    return score, level
