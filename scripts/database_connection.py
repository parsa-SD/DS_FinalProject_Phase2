import sqlite3
from pathlib import Path

def connect_db():
    # Go up one level from the "scripts" folder and into "database"
    db_path = Path(__file__).resolve().parent.parent / "database" / "nasdaq.db"
    conn = sqlite3.connect(str(db_path))
    return conn
