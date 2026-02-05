import streamlit as st

from nlp.clause_splitter import split_clauses
from risk.rules import detect_risks
from risk.scorer import calculate_risk_score

st.set_page_config(page_title="Contract Risk Bot", layout="wide")

st.title("📜 Contract Analysis & Risk Assessment Bot")
st.write("Upload or paste a contract to detect legal risks (SME-friendly, offline rules).")

contract_text = st.text_area(
    "Paste Contract Text Below",
    height=300,
    placeholder="Paste employment, vendor, lease, or service contract here..."
)

if st.button("Analyze Contract"):
    if not contract_text.strip():
        st.warning("Please paste contract text.")
    else:
        clauses = split_clauses(contract_text)

        all_risks = []
        for clause in clauses:
            risks = detect_risks(clause)
            all_risks.extend(risks)

        score, level = calculate_risk_score(all_risks)

        st.subheader("📊 Overall Risk Assessment")
        st.metric("Risk Score", score)
        st.metric("Risk Level", level)

        st.subheader("⚠️ Identified Risks")
        if not all_risks:
            st.success("No major risks detected.")
        else:
            for r in all_risks:
                st.error(f"**{r['severity']}** – {r['type']}\n\n{r['description']}")
