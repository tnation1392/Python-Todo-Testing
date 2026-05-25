from todo_logic import add_task, complete_task, delete_task, list_tasks
from storage import save_tasks, load_tasks

def main():
    tasks = load_tasks()
    next_id = max((task.id for task in tasks), default=0) + 1

    print("Simple Todo App (type 'help' for commands)")
    #Create a loop asking for user input
    while True:
        user_input = input(">>> ").strip()

    #creates the output for the help input
        if user_input == "help":
            print("Commands:")
            print("  add <description>")
            print("  list")
            print("  complete <id>")
            print("  delete <id>")
            print("  quit")
            continue

    #Creates the output for the add input
        if user_input.startswith("add "):
            description = user_input[4:]
            try:
                tasks, next_id = add_task(tasks, description, next_id)
                save_tasks(tasks)
                print("Task added.")
            except ValueError as e:
                print(f"Error: {e}")
            continue

    #Output for the list input
        if user_input == "list":
            output = list_tasks(tasks)
            if not output:
                print("No tasks.")
            else:
                for line in output:
                    print(line)
            continue

    #Output for the delete input
        if user_input.startswith("delete "):
            try:
                task_id = int(user_input.split()[1])
                tasks = delete_task(tasks, task_id)
                save_tasks(tasks)
                print("Task deleted.")
            except (ValueError, IndexError) as e:
                print(f"Error: {e}")
            continue

    #Output for the complete input
        if user_input.startswith("complete "):
            try:
                task_id = int(user_input.split()[1])
                tasks = complete_task(tasks, task_id)
                save_tasks(tasks)
                print("Task completed.")
            except (ValueError, IndexError) as e:
                print(f"Error: {e}")

            continue

        #Breaking the loop with the quit input
        if user_input == "quit":
            print("Goodbye!")
            break

        #Unkown input output
        print("Command not recognized. Type 'help' for commands")


if __name__ == "__main__":
    main()
