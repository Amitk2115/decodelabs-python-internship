# In-memory database to store all tasks
my_tasks = []

def add_task():
    task = input("Enter your task: ").strip()
    if task == "":
        print("Task cannot be empty!")
        return
    my_tasks.append(task)  # Adds task to the list
    print(f"'{task}' added!")

def view_tasks():
    if len(my_tasks) == 0:
        print("No tasks yet.")
        return
    for index, task in enumerate(my_tasks, start=1):  # enumerate gives index + value
        print(f"{index}. {task}")

def delete_task():
    view_tasks()
    if len(my_tasks) == 0:
        return
    try:
        num = int(input("Enter task number to delete: "))
        removed = my_tasks.pop(num - 1)  # pop() removes item by index
        print(f"'{removed}' deleted!")
    except (IndexError, ValueError):  # Handles wrong number or non-numeric input
        print("Invalid number.")

def main():
    while True:  # Keeps the program running until user quits
        print("\n1. Add task\n2. View tasks\n3. Delete task\n4. Quit")
        choice = input("Choice: ").strip()

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            break  # Exits the loop and ends the program
        else:
            print("Invalid choice.")

# Entry point: runs main() only when file is executed directly
if __name__ == "__main__":
    main()
