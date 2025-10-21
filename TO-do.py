"""
Simple persistent CLI To-Do app.

Features:
- Add, remove, view, clear tasks
- Tasks persisted in tasks.txt (same folder)
- Simple numeric removal and input validation
Run: python todo.py
"""
import os
import sys

TASKS_FILE = os.path.join(os.path.dirname(__file__), "tasks.txt")

def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, "r", encoding="utf-8") as f:
        return [line.rstrip("\n") for line in f if line.strip()]

def save_tasks(tasks):
    with open(TASKS_FILE, "w", encoding="utf-8") as f:
        for t in tasks:
            f.write(t + "\n")

def add_task(tasks):
    task = input("Enter task to add: ").strip()
    if not task:
        print("No text entered. Task not added.")
        return
    tasks.append(task)
    save_tasks(tasks)
    print("Task added.")

def view_tasks(tasks):
    if not tasks:
        print("No tasks.")
        return
    print("\nTo-Do List:")
    for i, t in enumerate(tasks, start=1):
        print(f"{i}. {t}")
    print()

def remove_task(tasks):
    if not tasks:
        print("No tasks to remove.")
        return
    view_tasks(tasks)
    idx = input("Enter task number to remove (or 'c' to cancel): ").strip().lower()
    if idx in ("c", "cancel"):
        print("Canceling.")
        return
    try:
        n = int(idx)
        if 1 <= n <= len(tasks):
            removed = tasks.pop(n - 1)
            save_tasks(tasks)
            print(f"Removed: {removed}")
        else:
            print("Number out of range.")
    except ValueError:
        print("Invalid number.")

def clear_tasks(tasks):
    confirm = input("Clear ALL tasks? (y/N): ").strip().lower()
    if confirm == "y":
        tasks.clear()
        save_tasks(tasks)
        print("All tasks cleared.")
    else:
        print("Abort clear.")

def main():
    tasks = load_tasks()
    menu = (
        "\nTo-Do CLI\n"
        "1) Add task\n"
        "2) Remove task\n"
        "3) View tasks\n"
        "4) Clear all tasks\n"
        "q) Quit\n"
    )
    while True:
        print(menu)
        choice = input("Choose an option: ").strip().lower()
        if choice in ("q", "quit", "exit"):
            print("Goodbye.")
            break
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            remove_task(tasks)
        elif choice == "3":
            view_tasks(tasks)
        elif choice == "4":
            clear_tasks(tasks)
        else:
            print("Invalid choice. Select 1-4 or q to quit.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nInterrupted. Exiting.")
        sys.exit(0)