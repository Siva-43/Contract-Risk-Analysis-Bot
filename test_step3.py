from nlp.text_extractor import extract_text
from nlp.clause_splitter import split_clauses
from nlp.classifier import classify_contract
from nlp.ner import extract_entities

file_path = "demo_contracts/sample.txt"

text = extract_text(file_path)

print("\n--- CONTRACT TYPE ---")
print(classify_contract(text))

print("\n--- ENTITIES ---")
entities = extract_entities(text)
for k, v in entities.items():
    print(f"{k}: {v}")

print("\n--- CLAUSES ---")
clauses = split_clauses(text)
for i, clause in enumerate(clauses, 1):
    print(f"\nClause {i}:")
    print(clause)
