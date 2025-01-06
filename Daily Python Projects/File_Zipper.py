import FreeSimpleGUI as FSGUI
from zip_creator import make_archive

label1 = FSGUI.Text("Select Files to compress")
input1 = FSGUI.Input()
choose_button1 = FSGUI.FilesBrowse("ChooseFile",key="files")

label2 = FSGUI.Text("Select Destination Folder")
input2 = FSGUI.Input()
choose_button2 = FSGUI.FolderBrowse("ChooseFolder",key="folder")
lbl_output = FSGUI.Text(key="output", text_color="green")


compress_button = FSGUI.Button("Compress")
window = FSGUI.Window("File Compressor",
                      layout=[
                          [label1, input1, choose_button1],
                          [label2, input2, choose_button2],
                          [compress_button, lbl_output]
                      ])

while True:
    event, values = window.read()
    print(event,values)
    filepaths = values["files"].split(";")
    folder = values["folder"]
    make_archive(filepaths, folder)
    window["output"].update(value="Compression Complete!")

    match event:
        case FSGUI.WIN_CLOSED:
            break


window.close()