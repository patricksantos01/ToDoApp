
while True:
    user_action = input("Type add, show, complete, edit or exit: ")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            # adding a \n to break a line in todos.txt
            todo = input("Enter a todo: ") + "\n"

            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            todos.append(todo)

            with open('todos.txt', 'w') as file:
                file.writelines(todos)

        case 'show':

            with open('todos.txt', 'r') as file:
                todos = file.readlines()
            
            for index, item in enumerate(todos):
                item = item.strip('\n')
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