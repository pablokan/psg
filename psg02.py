import PySimpleGUI as sg

def layout():
    return [
        [sg.InputText(key=f'input{x}') for x in range(5)], # comp list of inputs
        [sg.Text(size=(40,1), key='output')],
        [sg.Button('Show'), sg.Button('Exit')]
    ]

def main(window):                                                
    while True:
        event, values = window.read()
        if event in (sg.WINDOW_CLOSED, 'Exit'):
            break
        window['output'].update(f'{values["input3"]}')


if __name__ == '__main__':
    w = sg.Window('Window Title', layout())
    main(w)
    w.close()
