'''todos=[]
while True:
    user_action = input("Type add,show,edit,complete or exit:")
    match user_action:
        case 'add':
            todo=input("enter a todo") + "\n"
            todos.append(todo)
            file=open('todos.txt','w')
            file.writelines(todos)
        case 'show':
            for index,item in enumerate(todos):
                 row=(f"{index+1}-{item}")
                 print(row)

        case 'edit':
            number=int(input("enter a number of todo:"))
            number= number-1
            new_todo=input("enter a new todo:")
            todos[number]=new_todo
        case 'complete':
            number=int(input("enter a number of todo:"))
            number=number+1
            todos.pop(number)
        case 'exit':
            break
            print("bye!")'''

'''while True:
    user_action = input("Type add,show,edit,complete or exit:")
    match user_action:
        case 'add':
            todo=input("enter a todo") + "\n"

            file = open('todos.txt', 'r')
            todos=file.readlines()
            "after using it make sure to close at the end"
            file.close()

            todos.append(todo)

            file = open('todos.txt', 'w')
            file.writelines(todos)
            file.close()
        case'show':
            for index, item in enumerate(todos):
                row = (f"{index + 1}-{item}")
                print(row)

        case 'edit':
            number = int(input("enter a number of todo:"))
            number = number - 1
            new_todo = input("enter a new todo:")
            todos[number] = new_todo
        case 'complete':
            number = int(input("enter a number of todo:"))
            number = number + 1
            todos.pop(number)
        case 'exit':
            break
            print("bye!")'''


'''while True:
    user_action = input("Type add,show,edit,complete or exit:")
    match user_action:
        case 'add':
            todo=input("enter a todo") + "\n"

            file = open('file/subfiles/todos.txt', 'r')
            todos=file.readlines()
            "after using it make sure to close at the end"
            file.close()

            todos.append(todo)

            file = open('file/subfiles/todos.txt', 'w')
            file.writelines(todos)
            file.close()
        case'show':
            file = open('file/subfiles/todos.txt', 'r')
            todos = file.readlines()
            file.close()
            for index, item in enumerate(todos):
                row = (f"{index + 1}-{item}")
                print(row)

        case 'edit':
            number = int(input("enter a number of todo:"))
            number = number - 1
            new_todo = input("enter a new todo:")
            todos[number] = new_todo
        case 'complete':
            number = int(input("enter a number of todo:"))
            number = number + 1
            todos.pop(number)
        case 'exit':
            break
            print("bye!")'''
'''while True:
    user_action = input("Type add,show,edit,complete or exit:")
    match user_action:
        case 'add':
            todo=input("enter a todo") + "\n"

            file = open('file/subfiles/todos.txt', 'r')
            todos=file.readlines()
            "after using it make sure to close at the end"
            file.close()

            todos.append(todo)

            file = open('file/subfiles/todos.txt', 'w')
            file.writelines(todos)
            file.close()
        case'show':
            file = open('file/subfiles/todos.txt', 'r')
            todos = file.readlines()
            file.close()
            new_todos=[]
            for item in todos:
                new_item=item.strip("\n")
                new_todos.append(new_item)

            for index, item in enumerate(new_todos):
                row = (f"{index + 1}-{item}")
                print(row)

        case 'edit':
            number = int(input("enter a number of todo:"))
            number = number - 1
            new_todo = input("enter a new todo:")
            todos[number] = new_todo
        case 'complete':
            number = int(input("enter a number of todo:"))
            number = number + 1
            todos.pop(number)
        case 'exit':
            break
            print("bye!")'''
'''while True:
    user_action = input("Type add,show,edit,complete or exit:")
    match user_action:
        case 'add':
            todo=input("enter a todo") + "\n"

            with open("todos.txt",'r') as file:
                file.readlines(todos)

            todos.append(todo)

            with open('todos.txt', 'w') as file:
                todos=file.writelines()

        case 'show':
            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            for index, item in enumerate(todos):
                item=item.strip('\n')
                row = f"{index + 1}-{item}"
                print(row)

        case 'edit':
            number = int(input("enter a number of todo:"))
            number = number - 1
            with open("todos.txt",'r') as file:
                todos=file.readlines()
            print("here is todos existing:",todos)
            new_todo = input("enter a new todo:")
            todos[number] = new_todo
            with open("todos.txt",'w') as file:
                todos=file.writelines()

        case 'complete':
            number = int(input("enter a number of todo:"))
            number = number + 1
            todos.pop(number)
        case 'exit':
            break
            print("bye!")'''
'''while True:
    user_action = input("Type add,show,edit,complete or exit:")
    match user_action:
        case 'add':
            todo=input("enter a todo") + "\n"

            with  open('todos1.txt', 'r') as file:
                 todos=file.readlines()


            todos.append(todo)

            with open('todos1.txt', 'w') as file:
               file.writelines(todos)

        case'show':
            with open('todos1.txt', 'r') as file:
                todos=file.readlines()

            for index, item in enumerate(todos):
                new_item = item.strip("\n")
                row = (f"{index + 1}-{item}")
                print(row)

        case 'edit':
            number = int(input("enter a number of todo:"))
            number = number - 1
            with open('todos1.txt','r') as file:
                todos= file.readlines()
            print("here is the exisitng todo",todos)
            new_todo = input("enter a new todo:")
            todos[number] = new_todo+ '\n'

            print("here is how it will be",todos)

            with open('todos1.txt','w') as file:
                file.writelines(todos)
        case 'complete':
            number = int(input("enter a number of todo:"))
            with open('todos1.txt','r') as file:
                todos=file.readlines()
            index=number-1
            todo_to_remove=todos[index].strip('\n')
            todos.pop(index)
            with open('todos1.txt', 'w') as file:
                file.writelines(todos)
            message=f"Todo {todo_to_remove} was removed from the list"
            print(message)
        case 'exit':
            break
            print("bye!")'''
'''while True:
    user_action=input("Type add,show,edit,complete or exit:")
    match user_action:
        case 'add':
            todo = input("enter a todo:") + "\n"
            with open("todos1.txt",'r') as file:
                 todos = file.readlines()


            todos.append(todo)


            with open("todos1.txt", 'w') as file:
                file.writelines(todos)
        case 'show':
            with open("todos1.txt", 'r') as file:
                todos = file.readlines()
            for index, item in enumerate(todos):
                 new_item = item.strip('\n')
                 print(f"{index+1}-{item}")
        case 'edit':
            number=int(input("enter a no of todo you want to edit:"))
            number=number-1
            with open("todos1.txt", 'r') as file:
              todos = file.readlines()
            print("here is the existing todos:",todos)
            new_todo=input("enter a new todo:")
            todos[number-1]=new_todo + '\n'
            print("here is how it will be:",todos)


            with open("todos1.txt", 'w') as file:
                file.writelines(todos)
        case 'complete':
             number=int((input("enter a  no of todo that you want to complete:"))            
            with open("todos1.txt",'r') as file:
                todos=file.readlines()
            index = number - 1
            todo_to_remove=todos[index].strip('\n')
            todos.pop(index)
            with open("todos1.txt", 'w') as file:
                file.writelines(todos)
            message=f" Todo {todo_to_remove} was completed and removed from the list"
            print(message)
        case 'exit':

            print("bye!!")'''



'''while True:
    user_action=input("Type add,show,edit,complete or exit:")

    if 'add' in user_action:
        todo = user_action[4:]+ '\n'
        with open("todos1.txt",'r') as file:
             todos = file.readlines()


        todos.append(todo)


        with open("todos1.txt", 'w') as file:
            file.writelines(todos)
    elif 'show' in user_action:
        with open("todos1.txt", 'r') as file:
            todos = file.readlines()
        for index, item in enumerate(todos):
             new_item = item.strip('\n')
             print(f"{index+1}-{item}")
    elif 'edit' in user_action:
        number=int(user_action[5:])
        print(number)
        number=number-1
        with open("todos1.txt", 'r') as file:
          todos = file.readlines()
        print("here is the existing todos:",todos)
        new_todo=input("enter a new todo:")
        todos[number-1]=new_todo + '\n'
        print("here is how it will be:",todos)


        with open("todos1.txt", 'w') as file:
            file.writelines(todos)
    elif 'complete' in user_action:
        number=int(user_action[9:])
        with open("todos1.txt",'r') as file:
            todos=file.readlines()
        index = number - 1
        todo_to_remove=todos[index].strip('\n')
        todos.pop(index)
        with open("todos1.txt", 'w') as file:
            file.writelines(todos)
        message=f" Todo {todo_to_remove} was completed and removed from the list"
        print(message)
    elif 'exit' in user_action:
        print("bye!!")
    else:
        print("command not found!!")'''


'''with open('file/docx.txt','r') as file:
    content=file.read()
print(content)'''




'''while True:
    user_action=input("Type add,show,edit,complete or exit:")
    if 'add' in user_action:
    #if 'add' in user_action or 'more' in user_action or 'new' in user_action:
    #if 'add' in user_action and 'new' in user_action:
    #if 'add' not in user_action:
        todo = user_action[4:]+ '\n'
        with open("todos1.txt",'r') as file:
             todos = file.readlines()


        todos.append(todo)


        with open("todos1.txt", 'w') as file:
            file.writelines(todos)
    elif 'show' in user_action:
        with open("todos1.txt", 'r') as file:
            todos = file.readlines()
        for index, item in enumerate(todos):
             new_item = item.strip('\n')
             print(f"{index+1}-{item}")
    elif 'edit' in user_action:
        number=int(user_action[5:])
        print(number)
        number=number-1
        with open("todos1.txt", 'r') as file:
          todos = file.readlines()
        print("here is the existing todos:",todos)
        new_todo=input("enter a new todo:")
        todos[number-1]=new_todo + '\n'
        print("here is how it will be:",todos)


        with open("todos1.txt", 'w') as file:
            file.writelines(todos)
    elif 'complete' in user_action:
        number=int(user_action[9:])
        with open("todos1.txt",'r') as file:
            todos=file.readlines()
        index = number - 1
        todo_to_remove=todos[index].strip('\n')
        todos.pop(index)
        with open("todos1.txt", 'w') as file:
            file.writelines(todos)
        message=f" Todo {todo_to_remove} was completed and removed from the list"
        print(message)
    elif 'exit' in user_action:
        print("bye!!")
    else:
        print("command not found!!")'''


'''while True:
    user_action=input("Type add,show,edit,complete or exit:")
    if user_action.startswith('add'):
        todo = user_action[4:] + '\n'
        with open("todos1.txt",'r') as file:
             todos = file.readlines()


        todos.append(todo)


        with open("todos1.txt", 'w') as file:
            file.writelines(todos)
    elif user_action.startswith('show'):
        with open("todos1.txt", 'r') as file:
            todos = file.readlines()
        for index, item in enumerate(todos):
             new_item = item.strip('\n')
             print(f"{index+1}-{item}")
    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            print(number)

            number = number - 1

            with open("todos1.txt", 'r') as file:
               todos = file.readlines()
            print("here is the existing todos:", todos)

            new_todo = input("enter a new todo:")
            todos[number - 1] = new_todo + '\n'
            print("here is how it will be:", todos)

            with open("todos1.txt", 'w') as file:
               file.writelines(todos)
        except ValueError:
            print("command not valid!!!!!!!")
            continue

    elif user_action.startswith('complete'):
        try:
            number=int(user_action[9:])
            with open("todos1.txt",'r') as file:
               todos=file.readlines()

            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            with open("todos1.txt", 'w') as file:
               file.writelines(todos)

            message=f" Todo {todo_to_remove} was completed and removed from the list"
            print(message)
        except IndexError:
            print("There is no such item you mentioned")
            continue
    elif user_action.startswith('exit'):
        print("bye!!")
        break

    else:
        print("command not found!!")'''

def get_todos():
    with open("todos1.txt", 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local

'''while True:
    user_action=input("Type add,show,edit,complete or exit:")
    if user_action.startswith('add'):
        todo = user_action[4:] + '\n'
        todos=get_todos()


        todos.append(todo)


        with open("todos1.txt", 'w') as file:
            file.writelines(todos)
    elif user_action.startswith('show'):
        todos = get_todos()
        for index, item in enumerate(todos):
             new_item = item.strip('\n')
             print(f"{index+1}-{item}")
    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            print(number)

            number = number - 1

            todos = get_todos()
            print("here is the existing todos:", todos)

            new_todo = input("enter a new todo:")
            todos[number - 1] = new_todo + '\n'
            print("here is how it will be:", todos)

            with open("todos1.txt", 'w') as file:
               file.writelines(todos)
        except ValueError:
            print("command not valid!!!!!!!")
            continue

    elif user_action.startswith('complete'):
        try:
            number=int(user_action[9:])
            todos = get_todos()

            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            with open("todos1.txt", 'w') as file:
               file.writelines(todos)

            message=f" Todo {todo_to_remove} was completed and removed from the list"
            print(message)
        except IndexError:
            print("There is no such item you mentioned")
            continue
    elif user_action.startswith('exit'):
        print("bye!!")
        break

    else:
        print("command not found!!")'''


'''def get_todos(filepath):
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local

while True:
    user_action=input("Type add,show,edit,complete or exit:")
    if user_action.startswith('add'):
        todo = user_action[4:] + '\n'
        todos=get_todos("todos1.txt")


        todos.append(todo)


        with open("todos1.txt", 'w') as file:
            file.writelines(todos)
    elif user_action.startswith('show'):
        todos = get_todos("todos1.txt")
        for index, item in enumerate(todos):
             new_item = item.strip('\n')
             print(f"{index+1}-{item}")
    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            print(number)

            number = number - 1

            todos = get_todos("todos1.txt")
            print("here is the existing todos:", todos)

            new_todo = input("enter a new todo:")
            todos[number - 1] = new_todo + '\n'
            print("here is how it will be:", todos)

            with open("todos1.txt", 'w') as file:
               file.writelines(todos)
        except ValueError:
            print("command not valid!!!!!!!")
            continue

    elif user_action.startswith('complete'):
        try:
            number=int(user_action[9:])
            todos = get_todos("todos1.txt")

            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            with open("todos1.txt", 'w') as file:
               file.writelines(todos)

            message=f" Todo {todo_to_remove} was completed and removed from the list"
            print(message)
        except IndexError:
            print("There is no such item you mentioned")
            continue
    elif user_action.startswith('exit'):
        print("bye!!")
        break

    else:
        print("command not found!!")'''



'''def get_todos(filepath):
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local
def write_todos(filepath,todos_arg):
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)


while True:
    user_action=input("Type add,show,edit,complete or exit:")
    if user_action.startswith('add'):
        todo = user_action[4:] + '\n'
        todos=get_todos("todos1.txt")


        todos.append(todo)


        write_todos("todos1.txt",todos)
    elif user_action.startswith('show'):
        todos = get_todos("todos1.txt")
        for index, item in enumerate(todos):
             new_item = item.strip('\n')
             print(f"{index+1}-{item}")
    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            print(number)

            number = number - 1

            todos = get_todos("todos1.txt")
            print("here is the existing todos:", todos)

            new_todo = input("enter a new todo:")
            todos[number - 1] = new_todo + '\n'
            print("here is how it will be:", todos)

            write_todos("todos1.txt", todos)
        except ValueError:
            print("command not valid!!!!!!!")
            continue

    elif user_action.startswith('complete'):
        try:
            number=int(user_action[9:])
            todos = get_todos("todos1.txt")

            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            write_todos("todos1.txt", todos)

            message=f" Todo {todo_to_remove} was completed and removed from the list"
            print(message)
        except IndexError:
            print("There is no such item you mentioned")
            continue
    elif user_action.startswith('exit'):
        print("bye!!")
        break

    else:
        print("command not found!!")'''

def get_todos(filepath):
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return filepath
def write_todos(filepath,todos_arg):
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)


while True:
    user_action=input("Type add,show,edit,complete or exit:")
    if user_action.startswith('add'):
        todo = user_action[4:] + '\n'
        todos=get_todos("todos1.txt")


        todos.append(todo)


        write_todos("todos1.txt",todos)
    elif user_action.startswith('show'):
        todos = get_todos("todos1.txt")
        for index, item in enumerate(todos):
             new_item = item.strip('\n')
             print(f"{index+1}-{item}")
    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            print(number)

            number = number - 1

            todos = get_todos("todos1.txt")
            print("here is the existing todos:", todos)

            new_todo = input("enter a new todo:")
            todos[number - 1] = new_todo + '\n'
            print("here is how it will be:", todos)

            write_todos("todos1.txt", todos)
        except ValueError:
            print("command not valid!!!!!!!")
            continue

    elif user_action.startswith('complete'):
        try:
            number=int(user_action[9:])
            todos = get_todos("todos1.txt")

            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            write_todos("todos1.txt", todos)

            message=f" Todo {todo_to_remove} was completed and removed from the list"
            print(message)
        except IndexError:
            print("There is no such item you mentioned")
            continue
    elif user_action.startswith('exit'):
        print("bye!!")
        break

    else:
        print("command not found!!")































