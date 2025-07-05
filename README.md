# 🧪 Data Quality Monitoring Pipeline

A fully containerized data quality monitoring pipeline built with Python, Pandera, PostgreSQL, and Streamlit. This project fetches real-time data, validates schema expectations, logs results into a database, and visualizes data quality metrics via a dashboard.

---

## 🚀 Features

- 📥 **API Data Ingestion**: Pulls real-time data from public sources
- ✅ **Data Quality Checks**: Uses Pandera for schema and null validations
- 🗃 **Logging**: Stores validation results in PostgreSQL
- 📊 **Streamlit Dashboard**: Visualizes passed/failed checks in real-time
- 🐳 **Dockerized**: Entire app and database managed with Docker Compose

---

## 🧰 Tech Stack

- Python
- Pandera
- PostgreSQL
- Streamlit
- Docker & Docker Compose

---

## 📦 Folder Structure
dq_pipeline/
├── app/
│ ├── etl.py # Fetches and stores data
│ ├── dq_checks.py # Validates data and logs to DB
│ └── dashboard.py # Streamlit dashboard for monitoring
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
