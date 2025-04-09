# db.py
import sqlite3

DB_NAME = "tasks.db"

def get_connection():
    return sqlite3.connect(DB_NAME)

def init_db():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            completed BOOLEAN NOT NULL DEFAULT 0,
	    priority TEXT DEFAULT 'Medium',
            due_date TEXT
        )
    ''')
    conn.commit()
    conn.close()
