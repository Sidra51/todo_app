import functions
import FreeSimpleGUI as sg
label=sg.Text("Type in a to-do")
input_box=sg.InputText(tooltip="enter a todo",key="todo")
add_button=sg.Button("Add")
list_box=sg.Listbox(values=functions.get_todos(),key="todos",enable_events=True,size=(45,10))
edit_button=sg.Button("Edit")
complete_button=sg.Button("Complete")
#window=ss.Window('My To_do_app', layout=[[label,input_box]])
'''label amd input boc in one list so both will be in same row'''

window=sg.Window('My To_do_app', layout=[[label],[input_box],[add_button],[list_box,edit_button]],
                 font=('Helvetica',20))
'''now input and label both have diff list so there will be diffrent row'''

while True:
    event,values=window.read()
    print(1,event)
    print(2,values)
    print(3,values['todos'])
    match event:
         case "Add":
             todos=functions.get_todos()
             new_todo=values['todo'] + "\n"
             todos.append(new_todo)
             functions.write_todos(todos)
             window["todo"].update(value="todos")
         case "Edit":
             todo_to_edit=values['todos'][0]
             new_todo=values['todo']

             todos = functions.get_todos()
             index=todos.index(todo_to_edit)
             todos[index]=new_todo + "\n"
             functions.write_todos(todos)
             window[todos].update(values="todos") + "\n"
         case "todos":
             window["todo"].update(value=values["todos"][0])

         case sg.WIN_CLOSED:
             break

window.close()