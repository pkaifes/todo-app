import functions
#import tkinter - basic gui, not being used right now.
import FreeSimpleGUI as FSGUI

lbl_Intro = FSGUI.Text("Type in a to-do")
inp_Todo = FSGUI.InputText(tooltip="Enter todo", key="todo")
btn_add = FSGUI.Button("Add")
lst_todos = FSGUI.Listbox(values=functions.get_todos(), key="todos", enable_events=True, size=[45, 10])
btn_edit = FSGUI.Button("Edit")
btn_complete = FSGUI.Button("Complete")
btn_exit = FSGUI.Button("Exit")
window = FSGUI.Window('My To-Do App',
                      layout=[
                          [lbl_Intro],
                          [inp_Todo, btn_add],
                          [lst_todos, btn_edit, btn_complete],
                          [btn_exit]
                      ],
                      font=("Helvetica", 20)
                      )


while True:
    event, values = window.read() #open gui window
    print(event)
    print(values)

    match event:
        case "Add":
            todos = functions.get_todos()
            new_Todo = values["todo"] + "\n"
            todos.append(new_Todo)
            functions.write_todos(todos)
            window["todos"].update(values=todos)

        case "Edit":
            todo_to_edit = values["todos"][0]
            new_Todo = values["todo"]

            todos = functions.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_Todo + "\n"
            functions.write_todos(todos)

            window["todos"].update(values=todos)

        case "todos":
            window["todo"].update(value=values["todos"][0])
            #print("seen todos")
        case "Complete":
            todo_to_complete = values["todos"][0]
            todos = functions.get_todos()
            todos.remove(todo_to_complete)
            functions.write_todos(todos)

            window["todos"].update(values=todos)
            window["todo"].update(value="")

        case "Exit":
            break
        case FSGUI.WIN_CLOSED:
            break


window.close() #close gui window