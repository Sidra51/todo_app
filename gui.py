import functions
import FreeSimpleGUI as ss
label=ss.Text("Type in a to-do")
input_box=ss.InputText(tooltip="enter a todo")
add_button=ss.Button("add")
#window=ss.Window('My To_do_app', layout=[[label,input_box]])
'''label amd input boc in one list so both will be in same row'''
window=ss.Window('My To_do_app', layout=[[label],[input_box],[add_button]])
'''now input and label both have diff list so there will be diffrent row'''
window.read()
window.close()