# CLI Todo App (QA-Focused)

A command-line Todo application built in Python with a strong focus on:

- testability
- clean architecture
- QA automation practices

---

## Quick Overview

This project demonstrates:

- Unit, integration, and end-to-end testing
- JSON-based persistence
- CLI-based user interaction
- Real QA-style testing patterns

---

## Features

- Add tasks
- List tasks
- Complete tasks
- Delete tasks
- Persistent storage (JSON)
- Full pytest test suite

---

## Project Structure
The app is split into 3 layers:

### 🔹 Logic (`todo_logic.py`)
- Pure functions
- No input/output
- Easy to test

### 🔹 Storage (`storage.py`)
- Saves/loads JSON
- Handles missing/corrupted files

### 🔹 CLI (`cli.py`)
- User input/output
- Calls logic layer
- Handles errors

---

## ▶️ Run the App

```bash
python cli.py
```
## Commands
```
add <desc>     Add a task
list           Show tasks
complete <id>  Mark complete
delete <id>    Delete task
help           Show help
quit           Exit
```

## Run Tests

```
pip install pytest
pytest
```


