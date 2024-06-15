todos = []

while True:
    user_action = input("Type add, show, complete, edit or exit: ")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            # adding a \n to break a line in todos.txt
            todo = input("Enter a todo: ") + "\n"

            file = open('todos.txt', 'r')
            todos = file.readlines()
            file.close()

            todos.append(todo)

            file = open('todos.txt', 'w')
            file.writelines(todos)
            file.close()

        case 'show':
            file = open('todos.txt', 'r')
            todos = file.readlines()
            file.close()

            new_todos = [item.strip('\n') for item in todos ]

            for index, item in enumerate(new_todos):
                print(f"{index +1} -{item}")

        case 'edit':

            todo_number = int(input("Number of the todo to edit: "))
            todo_number = todo_number -1
            new_todo = input("Enter new todo: ")
            todos[todo_number] = new_todo

        case 'complete':
            todo_number = int(input("Number of the todo to complete: "))
            todos.pop(todo_number -1)
        case 'exit':
            break