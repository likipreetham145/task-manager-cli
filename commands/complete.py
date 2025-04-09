# commands/complete.py
from db import get_connection

def handle(task_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM tasks WHERE id = ?", (task_id,))
    task = cursor.fetchone()

    if not task:
        print(f"❌ No task found with ID {task_id}")
        return

    cursor.execute("UPDATE tasks SET completed = 1 WHERE id = ?", (task_id,))
    conn.commit()
    conn.close()

    print(f"✅ Task {task_id} marked as complete!")
