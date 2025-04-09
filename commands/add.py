# commands/add.py
from db import get_connection

def handle(title, priority='Medium', due_date=None):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO tasks (title, priority, due_date) VALUES (?, ?, ?)",
        (title, priority, due_date)
    )
    conn.commit()
    conn.close()
    print(f"✅ Task added: {title} | Priority: {priority} | Due: {due_date or 'N/A'}")
