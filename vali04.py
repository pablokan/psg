import PySimpleGUI as sg

layout = [  [sg.Text('Input only floating point numbers')],
            [sg.Input(key='-IN-')],
            [sg.Button('Nada', bind_return_key=True)],
            [sg.Text("", size=(40,1), key='-OUT-')],
            [sg.Button('Exit', key='Quit')]  ]

window = sg.Window('Floating point input validation', layout)

def valid_input(val):
    try:
        float(val)
        return True
    except ValueError:
        return False

while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Quit'):
        break
    if valid_input(values['-IN-']):
        window['-OUT-'].update(values['-IN-'])
        window['Quit'].SetFocus()
    else:
        window['-OUT-'].update('Debe ingresar un real')
        window['-IN-'].SetFocus()
window.close()
