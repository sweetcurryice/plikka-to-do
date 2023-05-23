import PySimpleGUI as ui

label1 = ui.Text("select file to compress :")
input1 = ui.Input()
button1 = ui.FilesBrowse("select")
label2 = ui.Text("select directory folder :")
input2 = ui.Input()
button2 = ui.FilesBrowse("select")
button_final = ui.Button("Compress")
display = ui.Window("File Compression", layout = [[label1, input1, button1], [label2, input2, button2], [button_final]])

display.read()
display.close()