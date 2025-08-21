# fastapi-task-manager
Task Manager API

A FastAPI-based Task Management API with CRUD operations and optional AI/voice assistant integration. This project includes automated testing using Gauge and follows PEP8 and clean code principles.

---

Project Structure:

task_manager/
├── app/
│   ├── __init__.py            # FastAPI app entrypoint
│   ├── main.py
│   ├── schemas.py             # Pydantic models
│   ├── crud.py                # CRUD operations
├── tests/
│   ├── specs/                 # Gauge specifications
│   │   └── task_management.spec
│   └── step_impl/             # Step implementations
│       └── steps.py
├── requirements.txt
└── README.txt

---

Features:

- CRUD operations for tasks: Create, Read, Update, Delete
- Task model with:
  - uuid: unique identifier
  - name: task name
  - description: optional description
  - status: created, in_progress, completed
- Swagger/OpenAPI documentation available at /docs
- In-memory storage (can be extended to database)
- Fully tested with Gauge and FastAPI TestClient

---

Setup Instructions:

1. Clone the repository:

git clone https://github.com/DavidCampbell8477/fastapi-task-manager.git
cd fastapi-task-manager

2. Create a virtual environment:

python -m venv venv
venv\Scripts\activate      

3. Install dependencies:

pip install -r requirements.txt

4. Run the FastAPI application:

uvicorn app.main:app --reload


---

Running Tests:

This project uses Gauge for automated testing.

1. Install Gauge and Python plugin:

gauge install python

2. Run the tests:

gauge run tests/specs/

All CRUD scenarios (Create, Read, Update, Delete) are covered.

---

Optional: Docker Setup

1. Build the Docker image:

docker build -t task_manager .

2. Run the container:

docker run -d -p 8000:8000 task_manager


---

Code Style & Quality:

- PEP8 compliant (black / flake8 )
- Clean code principles followed
- In-memory data storage is easy to replace with a database
- Gauge tests ensure API reliability and coverage

---

Future Improvements:

- Add database persistence (SQLite/PostgreSQL)
- Add filters, search, and pagination for task list
- Integrate with AI features like chatbots or voice assistants
- Add CI/CD workflow to run tests automatically

