
import functions
import PySimpleGUI as ui
todos = list
text = ui.Text("TO-DO creator")
display_todos = ui.Listbox(functions.readfile(), key = 'todos', enable_events= True, size=[45,10])
input_text = ui.InputText(tooltip="enter a todo", key = "todo", do_not_clear = True)
add_button = ui.Button("Add")
edit_button = ui.Button("Edit")
comp_button = ui.Button("Complete")
layout = [[text], [input_text],[add_button, edit_button, comp_button],[display_todos]]
window = ui.Window('hello mumuuu', layout = (layout))

while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            todos = functions.readfile()
            new_todo = values['todo'] + "\n"

            todos.append(new_todo)
            functions.writefile(todos)
            window["todos"].update(values = todos)
        case ui.WIN_CLOSED:
            break
        case "Edit":
            todo_edit = values["todos"][0]
            new_todo = values["todo"] + "\n"

            todos = functions.readfile()
            index = todos.index(todo_edit)
            todos[index] = new_todo

            functions.writefile(todos)
            window["todos"].update(values = todos)
        case "todos":
            if input_text.do_not_clear == False or values['todo'] =="":
                window["todo"].update(value = values['todos'][0])
        
        case "Complete":
            todo_complete = values['todos'][0]
            todos = functions.readfile()
            input_text.do_not_clear = False

            todos.remove(todo_complete)
            functions.writefile(todos)
            window["todos"].update(values = todos)
            

window.close()