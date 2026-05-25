from todo_logic import add_task, complete_task, delete_task, list_tasks

def main():
    tasks = []
    next_id = 1

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

        #Breaking the loop with the quit input
        if user_input == "quit":
            print("Goodbye!")
            break

        print("Command not recognized")


if __name__ == "__main__":
    main()
