from datetime import datetime

# Import validation functions
from task_manager.validation import validate_task_title, validate_task_description, validate_due_date

# Define tasks list
tasks = []

# Implement add_task function
def add_task(title, description, due_date):
    validate_task_title(title)
    validate_task_description(description)
    validate_due_date(due_date)
    
    task = {
            "title": title,
            "description": description,
            "due_date": due_date,
            "completed": False
        }
    tasks.append(task)
    print("Task added successfully!")
    
# Implement mark_task_as_complete function
def mark_task_as_complete(index, tasks=tasks):
    try:
        # Convert to zero-based index
        task = tasks[index - 1]
        
        # Mark as complete
        if task["completed"]:
            print("Task is already completed.")
        else:
            task["completed"] = True
            print("Task marked as complete!")    
    except IndexError:
        print("Invalid task number.")
# Implement view_pending_tasks function
def view_pending_tasks(tasks=tasks):
    pending_tasks = []

    # Step 1: Build the pending_tasks list manually
    for task in tasks:
        if not task["completed"]:
            pending_tasks.append(task)

    # Step 2: Check if there are no pending tasks
    if not pending_tasks:
        print("No pending tasks.")
        return

    # Step 3: Display pending tasks
    for index, task in enumerate(pending_tasks, start=1):
        print(f"\nTask {index}")
        print(f"Title: {task['title']}")
        print(f"Description: {task['description']}")
        print(f"Due Date: {task['due_date']}")
        print("Status: Pending")

# Implement calculate_progress function
def calculate_progress(tasks=tasks):
    if not tasks:
        return 0  # No tasks means 0% progress, to avoid division by 0

    total_tasks = len(tasks)
    completed_tasks = 0

    # Count completed tasks
    for task in tasks:
        if task["completed"]:
            completed_tasks += 1

    progress = (completed_tasks / total_tasks) * 100
    return progress