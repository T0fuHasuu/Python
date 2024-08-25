# To-Do List Application with Sample Tasks

def display_menu():
    print("\nTo-Do List Menu")
    print("1. View To-Do List")
    print("2. Remove Task")
    print("3. Exit")

def view_todo_list(todo_list):
    if not todo_list:
        print("\nYour to-do list is empty.")
    else:
        print("\nYour To-Do List:")
        for i, task in enumerate(todo_list, 1):
            print(f"{i}. {task}")

def remove_task(todo_list):
    view_todo_list(todo_list)
    if todo_list:
        try:
            task_number = int(input("\nEnter the number of the task to remove: "))
            if 1 <= task_number <= len(todo_list):
                removed_task = todo_list.pop(task_number - 1)
                print(f"Task '{removed_task}' removed from the list.")
                view_todo_list(todo_list)
            else:
                print("Invalid task number. Please try again.")
        except ValueError:
            print("Please enter a valid number.")

def main():
    # Sample tasks
    todo_list = [
        "Buy groceries",
        "Read a book",
        "Write code",
        "Go for a walk",
        "Call a friend"
    ]

    while True:
        display_menu()
        choice = input("\nEnter your choice: ")

        if choice == "1":
            view_todo_list(todo_list)
        elif choice == "2":
            remove_task(todo_list)
        elif choice == "3":
            print("Exiting To-Do List Application. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
