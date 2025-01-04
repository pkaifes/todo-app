import functions
#import tkinter - basic gui, not being used right now.
import FreeSimpleGUI as FSGUI

label = FSGUI.Text("Type in a to-do")
input_box = FSGUI.InputText(tooltip="Enter todo")
add_button = FSGUI.Button("Add")



window = FSGUI.Window('My To-Do App', layout=[[label], [input_box, add_button]])
window.read() #open gui window
window.close() #close gui window