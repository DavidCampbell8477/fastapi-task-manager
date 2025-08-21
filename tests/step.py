from getgauge.python import step, before_scenario
from fastapi.testclient import TestClient
from app.main import app
from uuid import UUID

# FastAPI test client
client = TestClient(app)

# Global storage to share data between steps
context = {}


@before_scenario
def reset_context(scenario):
    context.clear()


# ------------------ CREATE TASK ------------------ #
@step("Given I have a task with name <name> and description <description>")
def given_task(name, description):
    context["task_data"] = {"name": name, "description": description}


@step("When I send a POST request to /tasks/")
def post_task():
    response = client.post("/tasks/", json=context["task_data"])
    context["response"] = response
    context["task"] = response.json()


@step("Then the task is created successfully with status <status>")
def check_task_created(status):
    response = context["response"]
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    task = context["task"]
    assert task["status"] == status, f"Expected status '{status}', got '{task['status']}'"
    assert "uuid" in task


# ------------------ GET TASK ------------------ #
@step("When I send a GET request to /tasks/{uuid}")
def get_task_by_uuid(uuid):
    response = client.get(f"/tasks/{uuid}")
    context["response"] = response
    context["task"] = response.json()


@step("Then I should receive the task with name <name>")
def check_task_name(name):
    response = context["response"]
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    task = context["task"]
    assert task["name"] == name, f"Expected name '{name}', got '{task['name']}'"


# ------------------ GET TASK LIST ------------------ #
@step("When I send a GET request to /tasks/")
def get_task_list():
    response = client.get("/tasks/")
    context["response"] = response
    context["tasks"] = response.json()


@step("Then I should receive a list of tasks")
def check_task_list():
    tasks = context["tasks"]
    assert isinstance(tasks, list), f"Expected list, got {type(tasks)}"


# ------------------ UPDATE TASK ------------------ #
@step("When I send a PUT request to /tasks/{uuid} with status <status>")
def update_task(uuid, status):
    payload = {"status": status}
    response = client.put(f"/tasks/{uuid}", json=payload)
    context["response"] = response
    context["task"] = response.json()


@step("Then the task status should be <status>")
def check_task_status(status):
    task = context["task"]
    assert task["status"] == status, f"Expected status '{status}', got '{task['status']}'"


# ------------------ DELETE TASK ------------------ #
@step("When I send a DELETE request to /tasks/{uuid}")
def delete_task(uuid):
    response = client.delete(f"/tasks/{uuid}")
    context["response"] = response


@step("Then the task should be deleted successfully")
def check_task_deleted():
    response = context["response"]
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    data = response.json()
    assert data.get("detail") == "Task deleted successfully"
