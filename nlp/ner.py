import re

def extract_entities(contract_text: str) -> dict:
    entities = {
        "parties": [],
        "dates": [],
        "amounts": [],
        "jurisdiction": [],
        "duration": []
    }

    if not contract_text:
        return entities

    text = contract_text

    # --- Dates ---
    date_pattern = r"\b\d{1,2}\s+(January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{4}\b"
    entities["dates"] = re.findall(date_pattern, text)

    # --- Financial Amounts ---
    amount_pattern = r"(₹|Rs\.?|INR)\s?\d+(?:,\d+)*(?:\.\d+)?"
    entities["amounts"] = re.findall(amount_pattern, text)

    # --- Duration ---
    duration_pattern = r"\b\d+\s+(years?|months?|days?)\b"
    entities["duration"] = re.findall(duration_pattern, text.lower())

    # --- Jurisdiction ---
    if "laws of india" in text.lower():
        entities["jurisdiction"].append("India")

    # --- Parties (simple heuristic) ---
    party_pattern = r"\b(Employer|Employee|Company|Client|Vendor|Service Provider)\b"
    entities["parties"] = list(set(re.findall(party_pattern, text)))

    return entities
