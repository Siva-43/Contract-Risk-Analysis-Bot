def detect_risks(clause: str):
    clause_lower = clause.lower()
    risks = []

    # Unilateral termination
    if "terminate" in clause_lower and "without cause" in clause_lower:
        risks.append({
            "type": "Unilateral Termination",
            "severity": "High",
            "description": "One party can terminate the contract without giving a valid reason."
        })

    # Unlimited confidentiality
    if "confidential" in clause_lower and ("forever" in clause_lower or "at any time" in clause_lower):
        risks.append({
            "type": "Confidentiality Duration",
            "severity": "Medium",
            "description": "Confidentiality obligation has no clear time limit."
        })

    # Foreign governing law
    if "governed by" in clause_lower and "india" not in clause_lower:
        risks.append({
            "type": "Governing Law",
            "severity": "Low",
            "description": "Contract is governed by a foreign jurisdiction."
        })

    return risks
