# Enterprise Logistics Data Platform

An enterprise data platform designed to process, analyze, and visualize logistics data.

## Project Structure

*   `data/`: Directory for storing local data files (raw, processed, external).
*   `docs/`: Project documentation.
*   `images/`: Images and static assets.
*   `logs/`: Application log files.
*   `powerbi/`: Power BI templates, dashboards, and reporting models.
*   `python/`: Python modules, scripts, and utilities.
*   `sql/`: Raw SQL queries, schema definitions, and migration scripts.
*   `tests/`: Unit, integration, and end-to-end tests.
*   `dbt/`: DBT (Data Build Tool) project configuration and models.
*   `requirements.txt`: Python package dependencies.
*   `README.md`: Project documentation and guidelines.
*   `.gitignore`: Git ignore patterns.

## Setup Instructions

1.  **Clone the repository** (or navigate to this directory).
2.  **Set up a virtual environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```
3.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```
