📜 Contract Analysis & Risk Assessment Bot

A GenAI-inspired legal assistant designed to help Indian Small and Medium Enterprises (SMEs) understand complex contracts, identify legal risks, and take informed decisions — without requiring legal expertise.

This solution analyzes contracts such as employment agreements, vendor contracts, lease agreements, partnership deeds, and service contracts, and provides plain-language explanations, risk scoring, and actionable insights.

🚀 Problem Statement

Small and medium business owners often sign contracts without fully understanding:

Hidden legal risks

One-sided clauses

Compliance implications under Indian law

Legal advice is expensive and not always accessible. This project bridges that gap by providing an AI-assisted contract analysis tool that works locally, securely, and affordably.

🧠 Solution Overview

The Contract Risk Bot ingests contract text (PDF/DOC/TXT), breaks it down clause-by-clause, detects risky patterns using legal heuristics, and presents results in simple business language.

The system is designed to be:

SME-friendly

Confidential (no external legal databases)

Transparent (rule-based logic + audit logs)

Hackathon-compliant (no paid APIs required)

✨ Key Features
🔍 Core Legal NLP Capabilities

Contract type identification

Clause & sub-clause extraction

Named Entity Recognition (Parties, Dates, Amounts, Jurisdiction)

Obligation vs Right vs Prohibition detection

Ambiguity & risk flagging

⚠️ Risk Detection

Clause-level risk scoring (Low / Medium / High)

Contract-level composite risk score

Detection of:

Unilateral termination

Lock-in & auto-renewal

Non-compete clauses

Penalty & indemnity clauses

IP ownership transfer

Arbitration & jurisdiction clauses

📊 User Outputs

Simplified contract summary

Highlighted unfavorable clauses

Risk explanations in plain English

SME-friendly risk mitigation suggestions

Export-ready output for legal consultation

🌐 Multilingual Support

English & Hindi contract support

Internal normalization for analysis

Simple English output for business users

🏗️ System Architecture

contract-risk-bot/
│
├── app.py                      # Streamlit UI
├── nlp/                        # Text processing & NLP
│   ├── clause_splitter.py
│   ├── classifier.py
│   ├── ner.py
│
├── risk/                       # Legal risk logic
│   ├── rules.py
│   ├── scorer.py
│
├── llm/                        # Prompt design (optional extension)
│
├── utils/                      # Language handling, audit logs
│
├── data/
│   ├── templates/              # Standard SME contracts
│   └── logs/                   # JSON audit trails
│
└── demo_contracts/



🖥️ Live Demo

🔗 Live Application:
👉 (Add your Streamlit URL here)

📽️ Demo Video:
👉 (Add YouTube / Drive link here)

⚙️ Tech Stack

Language: Python

UI: Streamlit

NLP: spaCy, rule-based heuristics

Storage: Local files & JSON logs

Deployment: Streamlit Cloud

LLM: Optional (designed to work without paid APIs)

🔐 Privacy & Confidentiality

No contracts are sent to external legal databases

No case laws or statutes APIs used

All processing happens locally or within the deployed instance

Optional audit logs for traceability

📈 Future Enhancements

Advanced clause similarity using embeddings

Editable contract templates

Role-specific risk views (Founder / HR / Legal)

Multi-language UI support

Optional GenAI explanations using Claude / GPT-4

🏁 Hackathon Alignment

✔ Matches selected problem statement
✔ Uses allowed tooling stack
✔ No external legal data
✔ SME-focused
✔ Publicly accessible deployment
✔ Explainable & demo-ready
