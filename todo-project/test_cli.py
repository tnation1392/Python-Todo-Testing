import subprocess, sys, uuid, os,pytest

@pytest.fixture
def temp_file():
    filename = f"test_{uuid.uuid4().hex}.json"

    yield filename   # give it to the test

    # cleanup (runs after test!)
    if os.path.exists(filename):
        os.remove(filename)

def test_cli_add_and_list(temp_file):
    result = subprocess.run(
        [sys.executable, "cli.py", temp_file],
        input="add Learn testing\nlist\nquit\n",
        text=True,
        capture_output=True,
    )

    assert "[ ] 1: Learn testing" in result.stdout


import subprocess
import sys
import uuid
import os


def test_full_user_flow(temp_file):
    result = subprocess.run(
        [sys.executable, "cli.py", temp_file],
        input="add A\nadd B\ncomplete 1\nlist\nquit\n",
        text=True,
        capture_output=True,
    )

    output = result.stdout

    assert "[x] 1: A" in output
    assert "[ ] 2: B" in output


def test_data_persists_between_runs():
    filename = "test_tasks.json"

    # Ensure clean start
    if os.path.exists(filename):
        os.remove(filename)

    # Run 1: add task
    subprocess.run(
        [sys.executable, "cli.py", filename],
        input="add Save me\nquit\n",
        text=True,
    )

    # Run 2: verify
    result = subprocess.run(
        [sys.executable, "cli.py", filename],
        input="list\nquit\n",
        text=True,
        capture_output=True,
    )

    assert "Save me" in result.stdout

    os.remove(filename)

def test_invalid_complete(temp_file):
    result = subprocess.run(
        [sys.executable, "cli.py", temp_file],
        input="complete 999\nquit\n",
        text=True,
        capture_output=True,
    )

    assert "Error" in result.stdout
