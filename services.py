import requests
from models import db, Task
from config import EXTERNAL_API_URL

def fetch_external_status():
    """Fetch task status from the unreliable API (handles failures)."""
    try:
        response = requests.get(EXTERNAL_API_URL, timeout=1)  # 1-sec timeout
        if response.status_code == 200:
            data = response.json()
            return data.get("status", "pending")  # Default to 'pending'
    except requests.exceptions.RequestException:
        pass
    return "pending"

def create_task(title):
    """Create a new task with an external status."""
    status = fetch_external_status()
    task = Task(title=title, status=status)
    db.session.add(task)
    db.session.commit()
    return task

def get_tasks():
    """Retrieve all tasks from the database."""
    return Task.query.all()
