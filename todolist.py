
todo_list = []

while True:
    print("\n1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")
    
    choice = input("Choose an option: ")

    if choice == '1':
        task = input("Enter the task: ")
        todo_list.append(task)  
        print("Task added.")

    elif choice == '2':
        print("\nYour To-Do List:")
        for i in range(len(todo_list)):
            print(f"{i + 1}. {todo_list[i]}")

    elif choice == '3':
        task_num = int(input("Enter the task number to remove: ")) - 1
        if 0 <= task_num < len(todo_list):
            removed_task = todo_list.pop(task_num)
            print(f"Task '{removed_task}' removed.")
        else:
            print("Invalid task number.")

    elif choice == '4':
        print("bye bye!")
        break 
    else:
        print("Invalid choice, try again.")
