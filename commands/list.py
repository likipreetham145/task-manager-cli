# commands/list.py
from db import get_connection

def handle():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, title, completed, priority, due_date FROM tasks")
    rows = cursor.fetchall()
    conn.close()

    if not rows:
        print("📭 No tasks found.")
        return

    print("📝 Task List:")
    for row in rows:
        task_id = row[0]
        title = row[1]
        completed = row[2]
        priority = row[3] if len(row) > 3 else 'N/A'
        due_date = row[4] if len(row) > 4 else 'N/A'
        status = "✅" if completed else "❌"

        print(f"[{task_id}] {status} {title} | Priority: {priority} | Due: {due_date}")
