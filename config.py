import os

EXTERNAL_API_URL = "https://mitram-backend-7q7q.onrender.com/status"
DATABASE_URI = os.getenv("DATABASE_URI", "sqlite:///tasks.db")
