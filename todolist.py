#Create a simple command-line to-do list manager where users can add, remove, and view tasks.
todoList = []

def addToDo(task):
    todoList.append(task)
    print("Task successfully added")
    start()

def removeToDo(task):
    if task in todoList:
        todoList.remove(task)
        print("Task successfully removed")
    elif task not in todoList:
        print("Error: task not in list")
    start()

def viewAll():
    if todoList:
        print("To Do List:")
        for task in enumerate(todoList, start = 1):
            print(task)
    else:
        print("You have no tasks")
    start()

def menu():
    print("\nMenu")
    print("1. Add a task")
    print("2. Remove a task")
    print("3. View all tasks")
    print("4. Exit")

def start():
    menu()
    option = int(input("Please select an option: "))
    if option == 1:
        task = input("What task would you like to add? ")
        addToDo(task)

    elif option == 2:
        task = input("What task would you like to remove? ")
        removeToDo(task)

    elif option == 3:
        viewAll()

    elif option == 4:
        print("Program terminated")

    else:
        print("Error: Please select a valid option")
    
start()