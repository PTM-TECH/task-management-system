from datetime import datetime
import re

def validate_task_title(title):
    if not title:
        raise ValueError("Title can't be empty.")
    if not re.match(r'^[A-Za-z ]+$', title):
        raise ValueError("Title can only contain letters and spaces")
    
def validate_task_description(description):
    if not description:
        raise ValueError("Description can't be empty.")
    if not re.match(r'^[A-Za-z ]+$', description):
        raise ValueError("Description can only contain letters and spaces")   
    
def validate_due_date(due_date):
    if not due_date:
        raise ValueError("Due date can't be empty.")
    try:
        datetime.strptime(due_date, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Invalid date format. Please use YYYY-MM-DD.")