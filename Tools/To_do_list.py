# Printing Title starting point
print("To Do List") 

# Declare variable
list = []

# Option choosing
def options():
    print("""
Options :
    1. Display
    2. Add Task
    3. Complete Task
    4. Quit
          """)
# Display existing List
def display():
    print("\nTO DO LIST :")
    number = 0
    for task in list:
        number+=1
        print(f"{number}. {task}")

# Add new task
def AddTask():
    task = input("New Task: ")
    list.append(task)
    
# Mark list
def Pop():
    completed = int(input("Enter The Task Number : "))
    list.pop(completed-1)

# Looping the system
while True:
    options()
    choice = int(input("Choosing : "))
    if choice == 1:
        display()
    elif choice == 2:
        AddTask()
    elif choice == 3:
        Pop()
    else:
        break