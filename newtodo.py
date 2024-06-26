'''todos=[]
while True:
    user_action = input(type add,show,edit,complete and exit)
    match user_action:
        case 'add':
            todo=input("enter a todo")
            todos.append(todo)
        case 'show':
            for index,item in enumerate(todo):
                 row=(f"{index}-{item}")
                 print(row)
        case 'edit':
            number=int(input("enter a number of todo:"))
            number= number-1
            new_todo=input("enter a new todo:")
            todos[number]=new_todo
        case 'complete':
            number=int(input("enter a number of todo:")
            number=number+1
            todos.pop(number)
        case 'exit':
            break
            print("bye!")'''


'''todos=[]
while True:
    user_action = input("Type add,show,edit,complete or exit:")
    match user_action:
        case 'add':
            todo=input("enter a todo")
            todos.append(todo)
        case 'show':
            for index,item in enumerate(todos):
                 row=(f"{index}-{item}")
                 print(row)
            print(f"length is{index+1}")
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


while True:
    user_action = input("Type add,show,edit,complete or exit:")
    match user_action:
        case 'add':
            todo=input("enter a todo")
            todos.append(todo)
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
            print("bye!")