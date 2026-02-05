def split_clauses(text: str):
    clauses = []
    current = ""

    for line in text.split("\n"):
        if line.strip().startswith(tuple(str(i) for i in range(1, 20))):
            if current:
                clauses.append(current.strip())
            current = line
        else:
            current += " " + line

    if current:
        clauses.append(current.strip())

    return clauses
