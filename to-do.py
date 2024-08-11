import os

# File to store tasks
TODO_FILE = "todo_list.txt"

# Ensure the todo file exists
if not os.path.exists(TODO_FILE):
    with open(TODO_FILE, "w") as file:
        pass

def display_tasks():
    print("Your To-Do List:")
    if os.path.getsize(TODO_FILE) == 0:
        print("No tasks found.")
    else:
        with open(TODO_FILE, "r") as file:
            tasks = file.readlines()
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task.strip()}")

def add_task():
    task = input("Enter a new task: ")
    with open(TODO_FILE, "a") as file:
        file.write(task + "\n")
    print("Task added!")

def remove_task():
    display_tasks()
    try:
        task_num = int(input("Enter the number of the task to remove: "))
        with open(TODO_FILE, "r") as file:
            tasks = file.readlines()
        if 1 <= task_num <= len(tasks):
            removed_task = tasks.pop(task_num - 1)
            with open(TODO_FILE, "w") as file:
                file.writelines(tasks)
            print(f"Removed task: {removed_task.strip()}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    while True:
        print("\nTo-Do List Application")
        print("1. View tasks")
        print("2. Add a task")
        print("3. Remove a task")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            display_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            remove_task()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
