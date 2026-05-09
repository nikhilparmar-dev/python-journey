# Mini Project #8 -  To-Do List Application (Lists)
# Date: 24/02/2026
# Author: Nikhil

tasks = []

while True :

    print("\n===== TO-DO LIST MENU =====")
    print("1. Add Task")
    print("2. View Task")
    print("3. Delete Task")
    print("4. Update Task")
    print("5. Exit")

    choice = int(input("Enter Your Choice: "))

    if choice == 1 :

        task = input("Enter new Task: ") 
        tasks.append(task)
        print("Task Added Successfully!")


    elif choice == 2 : 

        if len(tasks) == 0 :
            print("No tasks available")
        else :
            print("\nYour Tasks: ")
            for i in range(len(tasks)) :
                print(i+1, ". ", tasks[i])


    elif choice == 3 :

        if len(tasks) == 0 :
            print("No tasks to delete!")
        else :
            for i in range(len(tasks)) :
                print(i+1, ". ", tasks[i])

            num = int(input("Enter task number to delete: "))

            if 1 <= num <= len(tasks) :
                tasks.pop(num - 1)
                print("Task Deleted successfully!")
            else :
                print("Invalid Number!")


    elif choice == 4 :

        if len(tasks) == 0 :
            print("No tasks to update!")
        else :
            for i in range(len(tasks)) :
                print(i+1, ". ", tasks[i])

            num = int(input("Enter task number to update: "))

            if 1 <= num <= len(tasks) :
                new_task = input("Enter Updated Task: ")
                tasks[num-1] = new_task
                print("Task Updated successfully!")
            else :
                print("Invalid Number!")


    elif choice == 5 :

        print("Thank You! Exiting program")
        break


    else :

        print("Invalid Choice! Please try again")

