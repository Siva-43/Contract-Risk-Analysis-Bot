def classify_contract(contract_text: str) -> str:
    text = contract_text.lower()

    if "employment" in text or "employee" in text or "employer" in text:
        return "Employment Agreement"

    if "lease" in text or "tenant" in text or "rent" in text:
        return "Lease Agreement"

    if "vendor" in text or "supplier" in text or "purchase order" in text:
        return "Vendor Contract"

    if "service" in text or "consultant" in text or "service provider" in text:
        return "Service Agreement"

    if "partnership" in text or "partners" in text:
        return "Partnership Deed"

    return "General Contract"
