import PySimpleGUI as sg

def layout():
    return [
        [sg.Text('Enter your name', size=(15, 1))],
        [sg.InputText(size=(40, 1), key='input')],
        [sg.Text(size=(40,1), key='output')],
        [sg.Button('Show'), sg.Button('Exit')]
    ]

def main(window):                                                
    while True:
        event, values = window.read()
        print(event, type(event), values, type(values))
        if event == sg.WINDOW_CLOSED or event == 'Exit':
            break
        window['output'].update(f'Hello {values["input"]} Thanks!', text_color='yellow')


if __name__ == '__main__':
    w = sg.Window('Window Title', layout())
    main(w)
    w.close()
