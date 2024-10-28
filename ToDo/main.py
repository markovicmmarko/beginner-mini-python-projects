
with open("todos.txt") as todos:
    todos = todos.readlines()

def display():
    with open("todos.txt") as file:
        file = file.read()
        file = file.split("\n")
    for i,t in enumerate(file):
        if t != "":
            print(f"{i+1}. {t}")
        else:
            break


while True:
    action = input("Type add, show, edit, remove or exit: ").lower().strip()

    if action == "exit":
        print("bye")
        break
    else:
        if action == "add":
            todo = input("Enter a todo: ")
            todos.append(todo.capitalize())
            with open("todos.txt", "a") as file:
                file.write(f"{todo.capitalize()}\n")
        elif action == "show":
            if len(todos) < 1:
                print("Empty todo list")
            else:
                display()
        elif action == "edit":
            display()
            todo_num = int(input("Enter a num of task which you want to change: "))
            new_todo = input("Enter your edited task: ")
            todos[todo_num-1] = new_todo.capitalize()
            with open("todos.txt") as file:
                file = file.readlines()
            file[todo_num-1] = new_todo.capitalize()
            with open("todos.txt", "w") as fajl:
                for x in file:
                    fajl.write(x)
            print("Edited!")
        elif action == "remove":
            display()
            task = int(input("Which task nr. is completed? "))
            todos.pop(task-1)
            with open("todos.txt", "w") as file:
                for todo in todos:
                    file.write(f"{todo}\n")
        else:
            print("Invalid action")


