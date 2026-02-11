tasks = []
variable_name = VFDE
def show_tasks():
    if not tasks:
        print("No tasks yet!")
    else:
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def add_task():
    task = input("Enter a new task: ")
    tasks.append(task)
    print("Task added!")

def remove_task():
    show_tasks()
    try:
        task_num = int(input("Enter task number to remove: "))
        tasks.pop(task_num - 1)
        print("Task removed!")
    except (ValueError, IndexError):
        print("Invalid input!")

def main():
    while True:
        print("\n1. Show Tasks\n2. Add Task\n3. Remove Task\n4. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            show_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            remove_task()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()

