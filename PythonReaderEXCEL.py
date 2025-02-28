import os
import pymysql
import pandas as pd
from datetime import datetime

# Database connection settings
DB_CONFIG = {
    "host": "your_host",      # Change this
    "user": "your_user",      # Change this
    "password": "your_pass",  # Change this
    "database": "your_db",    # Change this
    "port": 3306  # Default MySQL port
}

# Directory containing the Excel files
INPUT_DIR = "C:\\output\\in\\"

def connect_db():
    """Establishes a connection to the MySQL database."""
    return pymysql.connect(**DB_CONFIG)

def process_file(file_path):
    """Reads an Excel file and uploads data to MySQL."""
    try:
        df = pd.read_excel(file_path, engine='openpyxl')

        # Ensure columns match expected format
        if set(df.columns) != {"id", "hour", "agent", "case", "status"}:
            print(f"Skipping {file_path}: Invalid columns")
            return

        # Convert 'hour' column to timestamp
        df["hour"] = pd.to_datetime(df["hour"], errors='coerce')

        # Connect to DB
        conn = connect_db()
        cursor = conn.cursor()

        # Insert data into MySQL
        for _, row in df.iterrows():
            sql = """
                INSERT INTO FileReporter (id, hour, agent, case, status)
                VALUES (%s, %s, %s, %s, %s)
            """
            cursor.execute(sql, (row["id"], row["hour"], row["agent"], row["case"], row["status"]))

        # Commit and close connection
        conn.commit()
        cursor.close()
        conn.close()

        print(f"Successfully uploaded {file_path}")
    except Exception as e:
        print(f"Error processing {file_path}: {e}")

def main():
    """Scans the input directory for Excel files and processes them."""
    for file in os.listdir(INPUT_DIR):
        if file.endswith(".xlsx"):
            process_file(os.path.join(INPUT_DIR, file))

if __name__ == "__main__":
    main()