import functions
import FreeSimpleGUI as sg
label=sg.Text("Type in a to-do")
input_box=sg.InputText(tooltip="enter a todo",key="todo")
add_button=sg.Button("add")
#window=ss.Window('My To_do_app', layout=[[label,input_box]])
'''label amd input boc in one list so both will be in same row'''

window=sg.Window('My To_do_app', layout=[[label],[input_box],[add_button]],font=('Helvetica',30))
'''now input and label both have diff list so there will be diffrent row'''

while True:
    event,values=window.read()
    print(event)
    print(values)
    match event:
         case "add":
             todos=functions.get_todos()
             new_todo=values['todo'] + "\n"
             todos.append(new_todo)
             functions.write_todos(todos)
         case sg.WIN_CLOSED:
             break

window.close()