import PySimpleGUI as sg

layout = [  [sg.Text('Input only floating point numbers')],
            [sg.Input(key='-IN-')],
            [sg.Button('Nada', bind_return_key=True)],
            [sg.Text("", size=(40,1), key='-OUT-')],
            [sg.Button('Exit', key='Quit')]  ]

window = sg.Window('Floating point input validation', layout)

while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Quit'):
        break
    try:
        in_as_float = float(values['-IN-'])
        window['-OUT-'].update(values['-IN-'])
        window['Quit'].SetFocus()
    except:
        window['-OUT-'].update('Debe ingresar un real')
        window['-IN-'].SetFocus()
window.close()
