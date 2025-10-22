from app.database import init_db
from app.task_service import (
    get_db,
    add_task,
    list_tasks,
    mark_task_done,
    delete_task,
)

def main():
    # Initialize the database
    init_db()

    # Create a DB session using the get_db generator
    db_gen = get_db()
    db = next(db_gen)

    print("📝 Task Manager CLI")
    print("Commands: add <title> | list | done <id> | delete <id> | exit")

    while True:
        try:
            command = input(">>> ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nExiting.")
            break

        if not command:
            continue

        parts = command.split(maxsplit=1)
        action = parts[0]

        if action == "add":
            if len(parts) < 2:
                print("⚠️  Usage: add <title>")
                continue
            title = parts[1]
            task = add_task(db, title)
            print(f"✅ Added: {task.title} (id={task.id})")

        elif action == "list":
            tasks = list_tasks(db)
            if not tasks:
                print("📭 No tasks found.")
                continue
            for task in tasks:
                status = "✔️" if task.done else "❌"
                print(f"{task.id}: {task.title} [{status}]")

        elif action == "done":
            if len(parts) < 2 or not parts[1].isdigit():
                print("⚠️  Usage: done <id>")
                continue
            task_id = int(parts[1])
            success = mark_task_done(db, task_id)
            print("✅ Marked as done" if success else "❌ Task not found")

        elif action == "delete":
            if len(parts) < 2 or not parts[1].isdigit():
                print("⚠️  Usage: delete <id>")
                continue
            task_id = int(parts[1])
            success = delete_task(db, task_id)
            print("🗑️ Deleted" if success else "❌ Task not found")

        elif action == "exit":
            print("👋 Bye!")
            break

        else:
            print("❓ Unknown command")

    # Close the DB session
    db_gen.close()

if __name__ == "__main__":
    main()
