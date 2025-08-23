# Mark-Harper-CS-340
# Grazioso Salvare Dashboard (Project Two)

** Student:** Mark Harper
** Course:** CS-340  
** Term:** Fall 2025  
** Repository URL:** (https://github.com/MarkJamaicaAI/Mark-Harper-CS-340.git)

This repository contains my final dashboard code (Project Two) and the reusable **CRUD Python module** (from Project One) used to connect the dashboard widgets to the MongoDB database. The reflection below answers the journal questions and is included here so this repo can serve as a portfolio artifact.

---

## How to Run Locally

```bash
# 1) Create & activate a virtual environment
python -m venv .venv
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

# 2) Install dependencies
pip install -r requirements.txt

# 3) Configure environment variables (example)
# macOS/Linux:
export MONGO_URI="mongodb://username:password@host:port/?authSource=admin"
export DB_NAME="aac"
export COLLECTION_NAME="animals"
# Windows (PowerShell):
# $env:MONGO_URI="mongodb://..."
# $env:DB_NAME="aac"; $env:COLLECTION_NAME="animals"

# 4) Run the app
python app.py
