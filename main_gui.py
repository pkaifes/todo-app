import functions
#import tkinter - basic gui, not being used right now.
import FreeSimpleGUI as FSGUI

lbl_Intro = FSGUI.Text("Type in a to-do")
inp_Todo = FSGUI.InputText(tooltip="Enter todo", key="todo")
btn_add = FSGUI.Button("Add")



window = FSGUI.Window('My To-Do App',
                      layout=[[lbl_Intro], [inp_Todo, btn_add]],
                      font=("Helvetica", 20)
                      )


while True:
    event, values = window.read() #open gui window
    print(event)
    print(values)

    match event:
        case "Add":
            todos = functions.get_todos()
            new_Todo = values["todo"]
            todos.append(new_Todo)
            functions.write_todos(todos)
        case FSGUI.WIN_CLOSED:
            break


window.close() #close gui window