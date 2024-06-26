'''import FreeSimpleGUI as ss
label1=ss.Text("Enter feet:")
label2=ss.Text("Enter inches:")
input1=ss.InputText()
input2=ss.InputText()
convert_button=ss.Button("convert")
window=ss.Window("Converter",layout=[[label1,input1],[label2,input2],[convert_button]])
window.read()
window.close()'''

import FreeSimpleGUI as sg

label = sg.Text("What are dolphins?")
option1 = sg.Radio("Amphibians", group_id="question1")
option2 = sg.Radio("Fish", group_id="question1")
option3 = sg.Radio("Mammals", group_id="question1")
option4 = sg.Radio("Birds", group_id="question1")

window = sg.Window("File Compressor",layout=[[label],[option1,option2,option3,option4]])

window.read()
window.close()
