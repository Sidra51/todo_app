import FreeSimpleGUI as ss
label1=ss.Text("choose file to compress")
input1=ss.InputText()
button1=ss.FileBrowse("choose")
label2=ss.Text("choose destination folder:")
input2=ss.InputText()
button2=ss.FolderBrowse("choose")
compress_button=ss.Button("compress")
window=ss.Window("FILE COMPRESSOR",layout=[[label1,input1,button1],[label2,input2,button2],[compress_button]])
window.read()
window.close()
