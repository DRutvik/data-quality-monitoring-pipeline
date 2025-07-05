import streamlit as st
import psycopg2
import pandas as pd

def fetch_logs():
    try:
        conn = psycopg2.connect(
            dbname="dq_logs",
            user="user",
            password="password",
            host="localhost",
            port="5432"
        )
        df = pd.read_sql("SELECT * FROM dq_results", conn)
        conn.close()
        return df
    except Exception as e:
        st.error(f"❌ Error connecting to DB: {e}")
        return pd.DataFrame()

st.title("📊 Data Quality Monitoring Dashboard")

logs = fetch_logs()

if not logs.empty:
    st.success("✅ Loaded data quality logs from database.")
    st.dataframe(logs)
else:
    st.warning("⚠️ No data found. Have you run dq_checks.py yet?")
