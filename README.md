# 🚀 Real-Time Task Status Tracker with External API Integration

## 📌 Overview
This is a **Flask-based task tracking application** that integrates with an **external API** to fetch task statuses. If the API is unresponsive, the task status defaults to `"pending"`.

---

## ✨ Features
✅ **Task Management**: Create, retrieve, and update tasks.  
✅ **Database Integration**: Uses **SQLAlchemy** for storing tasks.  
✅ **External API Integration**: Fetches task status dynamically.  
✅ **Error Handling**: Defaults status to `"pending"` if API fails.  
✅ **Pydantic Validation**: Ensures input data validity.  
✅ **Basic Frontend**: Uses **Jinja2** for visualization.  
✅ **Docker Support**: **Containerized setup** for easy deployment.  
✅ **Testing Suite**: Includes **unit tests** to validate core functionality.  

---

## 💡 Design Choices
This project follows the **MVC (Model-View-Controller) pattern**, ensuring **scalability and maintainability**.

1. **Flask for Backend**  
   - Lightweight and easy to integrate.  
   - Manages API calls, database operations, and template rendering.  

2. **SQLite for Database**  
   - Simple and requires minimal setup.  
   - Supports efficient CRUD operations.  

3. **Jinja2 for Templating**  
   - Enables **dynamic content rendering** in HTML.  
   - Reduces frontend complexity.  

4. **Pydantic for Data Validation**  
   - Ensures user input matches the expected schema.  
   - Prevents invalid data from entering the database.  

5. **Docker for Deployment**  
   - Provides **containerization** for smooth cross-environment deployment.  
   - Ensures application consistency across different systems.  

---

## ⚡ Setup Instructions

### 1️⃣ Clone the Repository
```bash
git clone <repo-url>
cd task-tracker
```

### 2️⃣ Create and Activate Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate      # On Windows
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Set Up the Database
```bash
python init_db.py
```

### 5️⃣ Run the Flask App
```bash
python app.py
```

### 6️⃣ Access the App
Open **`http://127.0.0.1:5000`** in your browser.

---

## 🔗 API Endpoints
| Method | Endpoint       | Description          |
|--------|--------------|----------------------|
| `GET`  | `/tasks`      | Fetch all tasks     |
| `POST` | `/tasks`      | Create a new task   |

---

## 🧪 Testing Guidelines
This project includes **unit tests** to validate core functionality.

### Run Tests
```bash
pytest
```

### Testing Approach
- ✅ **Unit Tests**: Check individual functions for correctness.  
- ✅ **Integration Tests**: Ensure components work together properly.  
- ✅ **Mock API Calls**: Simulate API failures to test error handling.  

---

## 🚀 Docker Deployment
### 1️⃣ Build the Docker Image
```bash
docker build -t task-tracker .
```

### 2️⃣ Run the Docker Container
```bash
docker run -p 5000:5000 task-tracker
```

---

## 📂 Folder Structure
```
📂 task-tracker
├── 📂 templates        # Frontend HTML files
├── 📂 static           # CSS files
├── 📂 models           # Database models
├── 📂 services         # Business logic
├── app.py             # Main Flask app
├── requirements.txt   # Dependencies
├── Dockerfile         # Docker setup
├── tests.py           # Unit tests
└── README.md          # Project documentation
```

---

## 👤 Author
**Kunal Sharma**  

🔗 **LinkedIn**: [https://www.linkedin.com/in/kunal-sharma-8b9787334/](#)  
📧 **Email**: [kunalsharma7003@gmail.com](#)  

---

**🎯 Happy Coding! 🚀**
