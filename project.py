tasks = {}


def add_task():
    task_name=input("enter task name")
    task_priorty=input("enter task priorty")
    tasks[task_name]=task_priorty
    print(f"task{task_name} added with priorty {task_priorty}")


def view_tasks():
    if not  tasks:
        print("no tasks available")
    else:
        print("Current Tasks:")
        for task,priority, in tasks.items():
            print(f"-{task} (priority : {priority})")

def remove_task():
    task_to_remove=input("enter the task name to remove:")
    if task_to_remove in tasks:
        del tasks [task_to_remove]
        print(f"task {task_to_remove} removed.")
    else:
        print(f"task {task_to_remove} not found")


while True:
    print("\n task managment System")
    print("1 add task ")
    print("2 View tasks") 
    print("3 remove task")
    print("4 exit")

    choice=input("enter your choice(1,2,3,4)")

    if choice=="1":
        add_task()
    elif choice=="2":
        view_tasks()
    elif choice=="3":
        remove_task()
    elif choice=="4":
        print("exiting the task mangement system.goodbye")
        break
    else:
        print("only 1,2,3,4")
