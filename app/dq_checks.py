import pandas as pd
import pandera.pandas as pa
from pandera import Column, DataFrameSchema, Check
import psycopg2

def validate_data():
    df = pd.read_csv("data.csv")

    # Define schema
    schema = DataFrameSchema({
        "state": Column(str, Check(lambda s: s.notnull()))
    })

    try:
        validated_df = schema.validate(df)
        success = True
    except pa.errors.SchemaError as e:
        print(f"❌ Validation failed: {e}")
        success = False

    log_to_db("state_not_null", str(success))

def log_to_db(check_name, result):
    try:
        conn = psycopg2.connect(
            dbname="dq_logs", user="user", password="password", host="", port="5432"
        )
        cur = conn.cursor()

        cur.execute("""
            CREATE TABLE IF NOT EXISTS dq_results (
                check_name TEXT,
                result TEXT
            )
        """)

        cur.execute("INSERT INTO dq_results (check_name, result) VALUES (%s, %s)", (check_name, result))
        conn.commit()
        cur.close()
        conn.close()
        print(f"✅ Logged check '{check_name}' result: {result}")
    except Exception as e:
        print(f"❌ Failed to log result: {e}")

if __name__ == "__main__":
    validate_data()
