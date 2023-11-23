tasks = []
print(
    "These are the commands\n add -> add a task to the to-do list.\n complete -> mark a task as complete\n view all -> view the current tasks in the to-do list.\n view complete -> view all the completed tasks in the to-do list.\n view incomplete -> view all the incomplete tasks in the to-do list.\n help -> display all the help message.\n exit -> exit the program."
)

while True:
    try:
        command = input("Enter a command: ").lower()

        if command == "add":
            task_description = input("Enter task description: ")
            for task in tasks:
                if task["description"] == task_description:
                    print("Task already exists")
            tasks.append({"description": task_description, "status": "Incomplete"})

        elif command == "complete":
            task_number = int(input("Enter the task number to mark as complete: "))
            if task_number < 1 or task_number > len(tasks):
                print("Task not Found")
            else:
                tasks[task_number - 1]["status"] = "Completed"
                print(f"Task {task_number} is completed")
        elif command == "view all":
            if not tasks:
                print("No tasks in the list")
            else:
                for i, task in enumerate(tasks, 1):
                    print(f"{i}. {task['description']}-{task['status']}")
        elif command == "view complete":
            completed_tasks = [task for task in tasks if task["status"] == "Completed"]
            if not completed_tasks:
                print("No completed tasks")
            else:
                for i, task in enumerate(completed_tasks, 1):
                    print(f"{i}. {task['description']}")
        elif command == "view incomplete":
            incomplete_tasks = [
                task for task in tasks if task["status"] == "Incomplete"
            ]
            if not incomplete_tasks:
                print("No Incomplete tasks")
            else:
                for i, task in enumerate(incomplete_tasks, 1):
                    print(f"{i}. {task['description']}")
        elif command == "help":
            print(
                "These are the commands\n add -> add a task to the to-do list.\n complete -> mark a task as complete\n view all -> view the current tasks in the to-do list.\n view complete -> view all the completed tasks in the to-do list.\n view incomplete -> view all the incomplete tasks in the to-do list.\n help -> display all the help message.\n exit -> exit the program."
            )
        elif command == "exit":
            choice = input("Are you sure you want to exit? (yes/no): ").lower()
            if choice == "yes":
                print("Exiting the program....")
                break
        else:
            print("Invalid Command! Try 'help' to see available commands.")
    except ValueError:
        print("Enter a valid number for task operation")
    except Exception as e:
        print(f"An error occured: {e}")
