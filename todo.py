'''todos = []
while True:
    user_action= input("Type Add, Show or Exit:")
    match user_action:
        case 'Add':
            todo=input("Add the todo:")
            todos.append(todo)
        case 'Show':
            print(todos)
        case 'Exit':
            print("bye")
            break'''

'''todos = []
while True:
    user_action= input("Type Add, Show or Exit:")
    match user_action:
        case 'Add':
            todo=input("Add the todo:")
            todos.append(todo)
        case 'Show':
            for items in todos:
                print(items)

        case 'Exit':
            print("bye")'''

'''todos = []
while True:
    user_action= input("Type Add, Show or Exit:")
    user_actions= user_action.strip()
    match user_action:
        case 'Add':
            todo=input("Add the todo:")
            todos.append(todo)
        case 'Show':
            for items in todos:
                print(items)

        case 'Exit':
            print("bye")'''



'''todos = []
while True:
    user_action= input("Type Add, Show or Exit:")
    user_actions= user_action.strip()
    match user_action:
        case 'Add':
            todo=input("Add the todo:")
            todos.append(todo)
        case 'Show':
            for items in todos:
                print(items)
        case 'Exit':
            print("bye")
        case whatever:
             print("heyyyyy!!!!!!, yor entered wrong command")'''

'''todos = []
while True:
    user_action= input("Type Add, Show or Exit:")
    user_actions= user_action.strip()
    match user_action:
        case 'Add':
            todo=input("Add the todo:")
            todos.append(todo)
        case 'Show'| 'display':
            for items in todos:
                items=items.title()
                print(items)

        case 'Exit':
            print("bye")'''
'''todos=[]
while True:
        user_action=input("type add ,show,edit and :")
        user_action=user_action.strip()
        match user_action:
            case 'add':
                todo= input("enter a todo:")
                todos.append(todo)
            case 'show':
                for items in todos:
                    items= items.capitalize()
                    print(items)
            case 'edit':
                number= int(input("enter a number of todo:"))
                number=number-1
                existing_todo=todos[number]
                print(existing_todo)
            case 'exit':
                break
                print("bye!")'''

'''todos=[]
while True:
        user_action=input("type add ,show,edit and exit :")
        user_action=user_action.strip()
        match user_action:
            case 'add':
                todo= input("enter a todo:")
                todos.append(todo)
            case 'show':
                for index,items in enumerate(todos):

                    print(index,'-',items)
            case 'edit':
                number= int(input("enter a number of todo:"))
                number=number-1
                new_todo= input("enter a new todo:")
                todos[number]=new_todo

            case 'exit':
                break
                print("bye!")'''

todos=[]
while True:
        user_action=input("type add ,show,edit,complete and exit :")
        user_action=user_action.strip()
        match user_action:
            case 'add':
                todo= input("enter a todo:")
                todos.append(todo)
            case 'show':
                for index,items in enumerate(todos):
                    row=f"{index}-{items}"
                    print(row)
            case 'edit':
                number= int(input("enter a number of todo:"))
                number=number-1
                new_todo= input("enter a new todo:")
                todos[number]=new_todo
            case 'complete':
                number=int(input("enter the number of todos:"))
                todos.pop(number)

            case 'exit':
                break
                print("bye!")

