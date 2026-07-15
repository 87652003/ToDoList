import json
from datetime import datetime

#list to store all tasks
tasks=[]

def add_tasks():
    task = input("Enter Task: ")
    deadline = input("Enter deadline (YYYY-MM-DD) : ")
    priority = input("Enter priority (High/Medium/Low) : ")

    new_task = {
        "task" : task,
        "deadline" : deadline,
        "priority" : priority,
        "status" : "Pending"
    }

    tasks.append(new_task)
    save_tasks()
    print("Task Added Successfully!\n")

def view_tasks():
    if not tasks:
        print("No Tasks Available!")
        return
    print("\n -----------Tasks list------------")

    for i, task in enumerate(tasks, start=1):
        print(f"\n Task {i}")
        print(f"Name : {task['task']}")
        print(f"Deadline : {task['deadline']}")
        print(f"Priority : {task['priority']}")
        print(f"Status : {task['status']}")

def mark_complited():
    if not tasks:
        print("No Tasks Available!")
        return
    view_tasks()

    task_number = int(input("\n Enter task number to mark as complited: "))

    if 1 <= task_number <= len(tasks):
        tasks[task_number - 1]["status"] = "Completed"
        save_tasks()
        print("Task marked as completed!\n")
    else:
        print("Invalid Task number. \n")

def delete_task():
    if not tasks:
        print("No Tasks Available!")
        return
    view_tasks()

    task_number = int(input("\n Enter task number to Delete: "))

    if 1 <= task_number <= len(tasks):
        deleted = tasks.pop(task_number - 1)
        save_tasks()
        print(f"Task '{deleted['task']}' deleted successfully! \n ")
    else:
        print("Invalid task number \n")

    
def view_overdue_task():
    today = datetime.today()
    
    found = False

    print("\n ---------Overdue Tasks---------")

    for task in tasks:
        deadline = datetime.strptime(task["deadline"], "%Y-%m-%d")

        if deadline < today and task["status"] == "Pending":
            print(f"Task : {task['task']}")
            print(f"Deadline : {task['deadline']}")
            print(f"Priority : {task['priority']}")
            print(f"Status    : {task['status']}")
            print("------------------------------")

            found = True

        if not found:
            print("NO overdue tasks.\n")

def load_tasks():
    global tasks

    try:
        with open("tasks.json", "r") as file:
            tasks = json.load(file)

    except FileNotFoundError:
        tasks = []

def save_tasks():
    with open("tasks.json","w") as file:
        json.dump(tasks, file, indent=4)

load_tasks()

while True:
    print("\n ===== TO DO List ===== ")
    print("1. Add Task")
    print("2. View Task")
    print("3. Mark Task")
    print("4. Delete Task")
    print("5. View Overdue Task")
    print("6. Exit")

    choice = input("Enter Your Choice : " )

    if choice == "1":
        add_tasks()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        mark_complited()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        view_overdue_task()
    
    elif choice == "6":
        print("Thank you for using the TO DO List")    
        break
    else:
        print("Invalid choice, Try Again.")

