from flask import Flask, request, jsonify, render_template, redirect, url_for
from models import db, Task
from schemas import TaskCreateSchema, TaskResponseSchema
from database import init_db
from services import create_task, get_tasks

app = Flask(__name__)
init_db(app)  # Initialize Database

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        title = request.form.get("title")

        # ✅ Pydantic validation
        try:
            TaskCreateSchema(title=title)  # Validate title
        except ValueError as e:
            return f"Error: {e}", 400
        
        create_task(title)
        return redirect(url_for("home"))  # Redirect to prevent duplicate form submissions

    tasks = get_tasks()
    return render_template("index.html", tasks=[TaskResponseSchema(**task.__dict__).dict() for task in tasks])

if __name__ == "__main__":
    app.run(debug=True)
