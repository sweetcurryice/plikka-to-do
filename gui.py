
import functions
import PySimpleGUI as ui
todos = list
text = ui.Text("TO-DO creator")
display_todos = ui.Listbox(functions.readfile(), key = 'todos', enable_events= True, size=[45,10])
input_text = ui.InputText(tooltip="enter a todo", key = "todo")
button = ui.Button("Add")
button2 = ui.Button("Edit")
window = ui.Window('hello mumuuu', layout = [[text], [input_text],[button],[display_todos],[button2]])

while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            todos = functions.readfile()
            new_todo = values["todo"] + "\n"
            todos.append(new_todo)
            functions.writefile(todos)
            window["todos"].update(values = todos)
        case ui.WIN_CLOSED:
            break
        case "Edit":
            todo_edit = values["todos"][0]
            new_todo = values["todo"]

            todos = functions.readfile()
            index = todos.index(todo_edit)
            todos[index] = new_todo + "\n"

            functions.writefile(todos)
            window["todos"].update(values = todos)
        case "todos":
            window["todo"].update(value = values['todos'][0] )

window.close()