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

Reflection (Journal Q&A)
# 1) How do you write programs that are maintainable, readable, and adaptable?

I used separation of concerns and a reusable CRUD module:

crud.py encapsulates all database reads/writes behind clear functions (create, read, update, delete, plus query helpers).

The dashboard (app.py) only calls CRUD functions; UI code never deals with raw DB details.

I used descriptive names, small single-purpose functions, and docstrings to improve readability.

All configuration (like the Mongo connection string) lives in environment variables, not hard-coded values.

Advantages: Testing becomes easier, the UI and data layers can evolve independently, and I can reuse crud.py in a CLI tool or a future web/API service without rewriting database logic.

Future reuse: The module can power batch imports/exports, data-cleaning scripts, or a REST API (e.g., FastAPI) that multiple clients use.

# 2) How do you approach a problem as a computer scientist?

I worked requirements → data model → interfaces:

Clarified what Grazioso Salvare needs (filters, views, KPIs) and mapped that to a simple MongoDB schema with the right indexes.

Built iteratively: start with core “view/filter” flows, then add charts/interactions once queries are correct and fast.

Kept feedback loops short (test with realistic data, handle nulls/missing fields, verify edge cases).

Compared with earlier assignments, this project felt more product-oriented: I prioritized UX, performance, and maintainability.
Go-forward strategies: model from use-cases, isolate DB access, index the fields I query, parameterize config, and add quick integration tests for critical queries.

# 3) What do computer scientists do, and why does it matter?

I turn requirements and data into reliable systems that help organizations make better decisions.
This dashboard helps a company like Grazioso Salvare quickly filter/visualize adoptable animals and operational metrics, reducing manual steps and saving time. That enables faster matches, better resource allocation, and clearer visibility into the work—direct impact on outcomes.

