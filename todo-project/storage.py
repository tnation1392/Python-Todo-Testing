import json
from todo_logic import Task

#A function to save tasks in the list to a json
def save_tasks(tasks, filename="tasks.json"):
    data = []

    for task in tasks:
        data.append({
            "id": task.id,
            "description": task.description,
            "completed": task.completed
        })

    with open(filename, "w") as f:
        json.dump(data, f)


def load_tasks(filename="tasks.json"):
    try:
        with open(filename, "r") as f:
            data = json.load(f)

        tasks = []
        for item in data:
            tasks.append(
                Task(
                    id=item["id"],
                    description=item["description"],
                    completed=item["completed"]
                )
            )

        return tasks



    except (FileNotFoundError, json.JSONDecodeError):
        return []
