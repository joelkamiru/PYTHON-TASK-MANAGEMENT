from datetime import datetime
from .validation import validate_task_title, validate_task_description, validate_due_date

# Define tasks list
tasks = []

# Implement add_task function
def add_task(title, description, due_date):
    if (validate_task_title(title) and 
        validate_task_description(description) and 
        validate_due_date(due_date)):
        
        tasks.append({
            "title": title.strip(),
            "description": description.strip(),
            "due_date": due_date.strip(),
            "completed": False
        })
        print("Task added successfully!")
    
# Implement mark_task_as_complete function
def mark_task_as_complete(index, tasks=tasks):
    try:
        idx = int(index)
        if 0 <= idx < len(tasks) and not tasks[idx]["completed"]:
            tasks[idx]["completed"] = True
            print("Task marked as complete!")
        else:
            print("Error: Invalid index or task already completed.")
    except ValueError:
        print("Error: Please enter a valid numerical index.")
    
# Implement view_pending_tasks function
def view_pending_tasks(tasks=tasks):
    print("\n--- Pending Tasks ---")
    pending_exists = False
    for idx, task in enumerate(tasks):
        if not task["completed"]:
            print(f"[{idx}] {task['title']} (Due: {task['due_date']}) - {task['description']}")
            pending_exists = True
    if not pending_exists:
        print("No pending tasks.")

# Implement calculate_progress function
def calculate_progress(tasks=tasks):
    total = len(tasks)
    if total == 0:
        print("\nProgress: 0% (No tasks available)")
        return 0.0
        
    completed = sum(1 for t in tasks if t["completed"])
    progress = (completed / total) * 100
    print(f"\nProgress: {completed}/{total} tasks completed ({progress:.1f}%)")
    return progress