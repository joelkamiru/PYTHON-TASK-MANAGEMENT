from datetime import datetime

def validate_task_title(title):
    if not title or not title.strip():
        print("Error: Title cannot be empty.")
        return False
    return True
    
def validate_task_description(description):
    if not description or not description.strip():
        print("Error: Description cannot be empty.")
        return False
    return True   
    
def validate_due_date(due_date):
    try:
        datetime.strptime(due_date.strip(), "%Y-%m-%d")
        return True
    except ValueError:
        print("Error: Invalid date format. Use YYYY-MM-DD.")
        return False