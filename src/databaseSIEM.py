import sqlite3
from datetime import date, datetime

today = date.today()
period = date.today().strftime("%Y-%m")

DATABASE_META = "../data/siem/meta.db"
DATABASE_RAW = f"../data/siem/raw/raw_{period}.db"

def db_period_print():
    print(period)

def db_initialization():
    conn_meta = sqlite3.connect(DATABASE_META)
    cur_meta = conn_meta.cursor()

    cur_meta.execute("""
        CREATE TABLE IF NOT EXISTS logs_table(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            logs TEXT NOT NULL
        )
    """)

    conn_meta.commit()
    conn_meta.close()

    conn_raw = sqlite3.connect(DATABASE_RAW)
    cur_raw = conn_raw.cursor()

    cur_raw.execute("""
        CREATE TABLE IF NOT EXISTS raw_logs(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp INTEGER NOT NULL,
            source TEXT NOT NULL,
            raw_logs_payload TEXT NOT NULL
        ) 
    """)

    conn_raw.commit()
    cur_raw.close()

def db_write_raw(source, data):
    timestamp = datetime.now()
    conn = sqlite3.connect(DATABASE_RAW)
    conn.execute("INSERT INTO raw_logs (timestamp, source, raw_logs_payload) VALUES (?, ?, ?)", (timestamp, source, data,))
    conn.commit()
    conn.close()

def db_read_raw():
    conn = sqlite3.connect(DATABASE_RAW)
    cur = conn.execute("SELECT id, timestamp, source, raw_logs_payload FROM raw_logs")
    
    result = cur.fetchone()

    return result

