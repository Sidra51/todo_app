'''def get_todos(filepath="todos1.txt"):
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
        todos=get_todos()


        todos.append(todo)


        write_todos("todos1.txt",todos)
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

            write_todos("todos1.txt",todos)
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
import time

import functions

'''def get_todos(filepath="todos1.txt"):
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local
def write_todos(todos_arg,filepath):
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)


while True:
    user_action=input("Type add,show,edit,complete or exit:")
    if user_action.startswith('add'):
        todo = user_action[4:] + '\n'
        todos=get_todos()


        todos.append(todo)


        write_todos(filepath="todos1.txt",todos_arg=todos)
        #filepath=todos1.txt is actually default
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

            write_todos(filepath="todos1.txt",todos_arg=todos)
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

            write_todos(filepath="todos1.txt",todos_arg=todos)

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


'''from functions import get_todos ,write_todos
#import functions-just write todos=functions.get_todos() also functions.write_todos(todo)
while True:
    user_action=input("Type add,show,edit,complete or exit:")
    if user_action.startswith('add'):
        todo = user_action[4:] + '\n'
        todos=get_todos()


        todos.append(todo)


        #write_todos(filepath="todos1.txt",todos_arg=todos)
        write_todos(todos)
        #filepath=todos1.txt is actually default
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
            write_todos(todos)
            #write_todos(filepath="todos1.txt",todos_arg=todos)
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
            write_todos(todos)
            #write_todos(filepath="todos1.txt",todos_arg=todos)

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



'''import functions

while True:
    user_action=input("Type add,show,edit,complete or exit:")
    if user_action.startswith('add'):
        todo = user_action[4:] + '\n'
        todos= functions.get_todos()


        todos.append(todo)


        #write_todos(filepath="todos1.txt",todos_arg=todos)
        functions.write_todos(todos)
        #filepath=todos1.txt is actually default
        
    elif user_action.startswith('show'):
        todos = functions.get_todos()
        for index, item in enumerate(todos):
             new_item = item.strip('\n')
             print(f"{index+1}-{item}")
             
             
    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            print(number)

            number = number - 1

            todos = functions.get_todos()
            print("here is the existing todos:", todos)

            new_todo = input("enter a new todo:")
            todos[number - 1] = new_todo + '\n'
            print("here is how it will be:", todos)
            functions.write_todos(todos)
            #write_todos(filepath="todos1.txt",todos_arg=todos)
        except ValueError:
            print("command not valid!!!!!!!")
            continue

    elif user_action.startswith('complete'):
        try:
            number=int(user_action[9:])
            todos = functions.get_todos()

            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)
            functions.write_todos(todos)
            #write_todos(filepath="todos1.txt",todos_arg=todos)

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

import functions
import time
now=time.strftime("%B %d ,%Y %H:%M:%d")
print("it is",now)
while True:
    user_action=input("Type Add,show,edit,complete,exit:")
    if user_action.startswith("add"):
        todo=user_action[4:] + "\n"
        todos=functions.get_todos()


        todos.append(todo)

        functions.write_todos(todos)




    elif user_action.startswith("show"):
         todos=functions.get_todos()
         for index,items in enumerate(todos):
              new_items=items.strip("\n")
              print(f"{index+1}-{new_items}")





    elif user_action.startswith("edit"):
        try:
            number=int(user_action[5:])
            number=number-1
            print(number)
            todos=functions.get_todos()
            print("here is your existing todo",todos)
            new_todo=input("enter a new todo:")
            todos[number-1] = new_todo + "\n"
            print("heres it how it will be:",todos)
            functions.write_todos(todos)
        except ValueError:
           print("sorry")
           continue


    elif user_action.startswith("complete"):
        try:
            number=int(user_action[9:])
            number=number-1
            todos=functions.get_todos()
            index=number-1
            todo_to_remove=todos[index].strip("\n")
            todos.pop(index)
            functions.write_todos(todos)
            message=f"Todo {todo_to_remove} was completed and hence removed from the list"
            print(message)
        except IndexError:
            print("sorry  not found")
            continue
    elif user_action.startswith("exit"):
        print("bye")
        break
    else:
        print("command not found")








