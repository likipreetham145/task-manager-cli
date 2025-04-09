import sys
from db import init_db
from commands import add, list, complete, delete

def show_help():
    print("""
Task Manager CLI

Usage:
    python main.py add "Task title" [--priority=High|Medium|Low] [--due=YYYY-MM-DD]
    python main.py list
    python main.py complete <task_id>
    python main.py delete <task_id>

Examples:
    python main.py add "Submit assignment" --priority=High --due=2025-04-10
    python main.py complete 2
    python main.py list
""")

def main():
    init_db()

    if len(sys.argv) < 2:
        show_help()
        return

    command = sys.argv[1]

    if command == "add" and len(sys.argv) >= 3:
        task_title = sys.argv[2]
        priority = "Medium"
        due_date = None

        for arg in sys.argv[3:]:
            if arg.startswith("--priority="):
                priority = arg.split("=", 1)[1]
            elif arg.startswith("--due="):
                due_date = arg.split("=", 1)[1]

        add.handle(task_title, priority, due_date)

    elif command == "list":
        list.handle()

    elif command == "complete" and len(sys.argv) == 3:
        complete.handle(sys.argv[2])

    elif command == "delete" and len(sys.argv) == 3:
        delete.handle(sys.argv[2])

    else:
        show_help()

if __name__ == "__main__":
    main()
