import PySimpleGUI as sg


def main():
    layout = [[sg.Button("Open Window", key="open")]]
    window = sg.Window("Main Window", layout)
    while True:
        event, values = window.read()
        if event in ("Exit", sg.WIN_CLOSED):
            break
        if event == "open":
            window2 = sg.Window("Other Window", [[sg.Text("Otra ventana")]])
            window.close()
            window2.read()


if __name__ == "__main__":
    main()
