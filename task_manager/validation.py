from datetime import datetime
import re

def validate_task_title(title):
    if len(title) == 0:
        raise ValueError("Title can't be empty.")
    if len(title) > 100:
        raise ValueError("Title too long")
    if not re.match(r'^[A-Za-z0-9 ]+$', title):
        raise ValueError("Title can only contain letters, numbers, and spaces")
    
def validate_task_description(description):
    if len(description) == 0:
        raise ValueError("Description can't be empty.")
    if len(description) > 500:
        raise ValueError("Description too long")
    if not re.match(r'^[A-Za-z0-9 ]+$', description):
        raise ValueError("Description can only contain letters, numbers, and spaces")   
    
def validate_due_date(due_date):
    if len(due_date) == 0:
        raise ValueError("Due date can't be empty.")
    try:
        datetime.strptime(due_date, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Invalid date format. Please use YYYY-MM-DD.")