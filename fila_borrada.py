import PySimpleGUI as sg


def make_window(fila_deleteada):
    # ------------------- Layout Definition -------------------
    layout = [
        [sg.Text("This is your layout")],
        [sg.Input(key="-IN-")],
        [sg.Text("You typed:"), sg.Text(size=(20, 1), key="-OUT-")],
        [sg.Button("Go"), sg.Button("Dark Gray 13 Theme"), sg.Button("Exit")],
    ]
    if fila_deleteada != None:
        layout.pop(fila_deleteada)
    # ------------------- Window Creation -------------------
    return sg.Window("Window Title", layout)


def main():

    window = make_window(None)  # create the window

    while True:
        event, values = window.read()
        print(event, values)
        if event == sg.WIN_CLOSED or event == "Exit":
            break
        if event == "Go":
            # change the "output" element to be the value of "input" element
            window["-OUT-"].update(values["-IN-"])
        elif event.startswith("Dark"):
            sg.theme("Dark Gray 13")
            window.close()  # close the window
            window = make_window(0)  # make a new window with the "same layout"

    window.close()


if __name__ == "__main__":
    main()
