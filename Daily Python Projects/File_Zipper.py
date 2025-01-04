import FreeSimpleGUI as FSGUI

label1 = FSGUI.Text("Select Files to compress")
input1 = FSGUI.Input()
choose_button1 = FSGUI.FilesBrowse("Choose")

label2 = FSGUI.Text("Select Destination Folder")
input2 = FSGUI.Input()
choose_button2 = FSGUI.FolderBrowse("Choose")

compress_button = FSGUI.Button("Compress")
window = FSGUI.Window("File Compressor",
                      layout=[
                          [label1, input1, choose_button1],
                          [label2, input2, choose_button2],
                          [compress_button]
                      ])

window.read()
window.close()