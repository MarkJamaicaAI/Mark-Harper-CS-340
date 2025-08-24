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
```
# Reflection (Journal Q&A)
I approached this project the way I approach most real-world software: start from what the user needs, then design the data and interfaces to make those outcomes reliable. For the Grazioso Salvare dashboard, I mapped their questions (filters and views) to a simple document structure and added indexes on the fields used most. The UI (dashboard) and the data layer (CRUD module) were intentionally decoupled. The dashboard handled input validation and visualization; crud.py handled all database interactions behind clear functions. That separation made the codebase maintainable (each part has a single responsibility), readable (small, well-named functions with docstrings), and adaptable (I can change queries or even swap databases with minimal UI changes). I kept credentials in environment variables, pinned dependencies, and added basic logging and error handling so failures are traceable.

Working this way had tangible advantages. It simplified testing, made the dashboard code much cleaner, and created a reusable CRUD layer that I can drop into other projects, such as a small FastAPI service, batch import/export scripts, or analytics notebooks. Compared with earlier assignments, this felt more product-focused: I made practical tradeoffs (e.g., denormalizing some fields for faster reads), ensured the most important paths were performant, and thought about maintainability from the start. Going forward, I’ll keep using the same strategy: derive the data model from user stories, select the right storage technology, define validation and indexes early, automate seeds/migrations, and add a few integration tests for the core queries.

At a higher level, this is what computer scientists do: we convert requirements and data into dependable systems that make people more effective. For a company like Grazioso Salvare, the dashboard removes manual steps and gives them fast, trustworthy insight—helping staff match animals to adopters more quickly, track operations with less friction, and ultimately improve outcomes.

