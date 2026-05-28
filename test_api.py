import pytest, requests
import threading
from app import app


@pytest.fixture(scope="module")
def client():
    server = threading.Thread(target=app.run, kwargs={"port": 5001})
    server.daemon = True
    server.start()

    yield "http://127.0.0.1:5001"

def test_get_tasks_empty(client):
    response = requests.get(f"{client}/tasks")

    assert response.status_code == 200
    assert response.json() == []

def test_create_task(client):
    response = requests.post(
        f"{client}/tasks",
        json={"description": "Test task"}
    )

    data = response.json()

    assert response.status_code == 201
    assert data["description"] == "Test task"
    assert data["completed"] is False

def test_full_flow(client):
    # create
    res1 = requests.post(
        f"{client}/tasks",
        json={"description": "Task A"}
    )
    task_id = res1.json()["id"]

    # complete
    res2 = requests.post(f"{client}/tasks/{task_id}/complete")

    # list
    res3 = requests.get(f"{client}/tasks")

    assert res2.status_code == 200
    assert any(t["completed"] for t in res3.json())


@pytest.fixture(scope="module")
def client():
    server = threading.Thread(target=app.run, kwargs={"port": 5001})
    server.daemon = True
    server.start()

    base_url = "http://127.0.0.1:5001"

    yield base_url

@pytest.fixture(autouse=True)
def reset_api(client):
    requests.post(f"{client}/reset")
