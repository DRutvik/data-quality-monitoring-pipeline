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
``` dq_pipeline/ ├── app/ │ ├── etl.py # Fetches and stores data │ ├── dq_checks.py # Validates data and logs to DB │ └── dashboard.py # Streamlit dashboard for monitoring ├── data.csv ├── Dockerfile ├── docker-compose.yml ├── requirements.txt └── README.md ```

---

## 🖼 Screenshot 
<img width="1470" alt="Screenshot 2025-07-05 at 1 15 24 PM" src="https://github.com/user-attachments/assets/6ccab11e-2bf3-48fc-a4c2-86ac73674f0c" />





