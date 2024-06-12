todos = []

while True:
    user_action = input("Type add, show, complete, edit or exit: ")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input("Enter a todo: ")
            todos.append(todo)
        case 'show':
            for index, item in enumerate(todos):
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