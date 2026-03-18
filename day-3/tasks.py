import json
import sys
from datetime import datetime

class TaskManager:
    FILE_NAME = "tasks.json"

    def __init__(self):
        self.tasks = self.load_tasks()

    # ---------- Persistence ----------
    def load_tasks(self):
        try:
            with open(self.FILE_NAME, "r") as f:
                return json.load(f)
        except FileNotFoundError:
            return []
        except json.JSONDecodeError:
            print("Error: tasks.json is corrupt. Starting fresh.")
            return []

    def save_tasks(self):
        with open(self.FILE_NAME, "w") as f:
            json.dump(self.tasks, f, indent=2)

    # ---------- Core Features ----------
    def add_task(self, title):
        new_id = 1 if not self.tasks else self.tasks[-1]["id"] + 1
        task = {
            "id": new_id,
            "title": title,
            "status": "todo",
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        self.tasks.append(task)
        self.save_tasks()
        print(f"Task added with id={new_id}")

    def complete_task(self, task_id):
        task = self.find_task(task_id)
        if task:
            task["status"] = "done"
            self.save_tasks()
            print(f"Task {task_id} marked as done")
        else:
            print(f"Task {task_id} not found")

    def delete_task(self, task_id):
        task = self.find_task(task_id)
        if task:
            self.tasks.remove(task)
            self.save_tasks()
            print(f"Task {task_id} deleted")
        else:
            print(f"Task {task_id} not found")

    def list_tasks(self, filter_status=None):
        tasks_to_show = self.tasks
        if filter_status:
            tasks_to_show = [t for t in self.tasks if t["status"] == filter_status]

        if not tasks_to_show:
            print("No tasks found")
            return

        print("\nID | Status | Title | Created")
        print("-" * 50)
        for t in tasks_to_show:
            print(f"{t['id']:2} | {t['status']:5} | {t['title']} | {t['created_at']}")

    # ---------- Helper ----------
    def find_task(self, task_id):
        return next((t for t in self.tasks if t["id"] == task_id), None)


# ---------- CLI ----------
def main():
    tm = TaskManager()

    if len(sys.argv) < 2:
        print("Usage: add | done | delete | list")
        return

    command = sys.argv[1].lower()

    try:
        if command == "add":
            if len(sys.argv) < 3:
                print("Please provide a task title")
            else:
                title = " ".join(sys.argv[2:])
                tm.add_task(title)

        elif command == "done":
            task_id = int(sys.argv[2])
            tm.complete_task(task_id)

        elif command == "delete":
            task_id = int(sys.argv[2])
            tm.delete_task(task_id)

        elif command == "list":
            if len(sys.argv) == 4 and sys.argv[2] == "--filter":
                tm.list_tasks(sys.argv[3])
            else:
                tm.list_tasks()
        else:
            print(f"Unknown command: {command}")

    except IndexError:
        print("Missing arguments")
    except ValueError:
        print("Task ID must be a number")


if __name__ == "__main__":
    main()