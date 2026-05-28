import pytest

#A function testing that the save and load tasks works
def test_save_and_load_tasks():
    from storage import save_tasks, load_tasks
    from todo_logic import Task
    import os

    filename = "test_tasks.json"

    tasks = [Task(1, "Test", False)]
    save_tasks(tasks, filename)

    loaded = load_tasks(filename)

    assert len(loaded) == 1
    assert loaded[0].id == 1
    assert loaded[0].description == "Test"

    os.remove(filename)

#A function testing that loading a missing file returns an empty list
def test_load_missing_file_returns_empty():
    from storage import load_tasks

    tasks = load_tasks("does_not_exist.json")

    assert tasks == []

#A function testing a corrupted file
def test_load_corrupted_file():
    from storage import load_tasks
    import os

    filename = "bad.json"

    with open(filename, "w") as f:
        f.write("{ bad json")

    tasks = load_tasks(filename)
    assert tasks == []
    os.remove(filename)