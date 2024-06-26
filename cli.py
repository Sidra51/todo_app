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
