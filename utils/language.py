def detect_language(text: str) -> str:
    """
    Detects whether text is English or Hindi based on Unicode range.
    """

    if not text:
        return "Unknown"

    for char in text:
        if "\u0900" <= char <= "\u097F":
            return "Hindi"

    return "English"


def normalize_text(text: str) -> str:
    """
    Normalizes text for downstream NLP tasks.
    Currently performs basic cleanup.
    """

    if not text:
        return ""

    return text.replace("\r", "").strip()
