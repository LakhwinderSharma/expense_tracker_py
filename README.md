# Expense Tracker API

A simple REST API built with **FastAPI** that loads expense data from a JSON file and exposes endpoints to retrieve expenses by month.

## Prerequisites

Before you begin, make sure you have the following installed:

* Python 3.12 or later
* `uv`

Verify the installations:

python --version

uv --version

# Install Dependencies
uv sync

This command installs all dependencies defined in `pyproject.toml` and `uv.lock`.

# Run the Application
uv run uvicorn app.main:app --reload

# API Endpoint
## Get Expenses by Month

**Request**
GET /expenses/{month}

### Run the application
uv run uvicorn app.main:app --reload

### List installed packages
uv pip list

### Display dependency tree
uv tree

