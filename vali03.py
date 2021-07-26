import PySimpleGUI as sg

layout = [  [sg.Text('Input only floating point numbers')],
            [sg.Input(key='-IN-')],
            [sg.Button('Nada')],
            [sg.Button('Exit')]  ]

window = sg.Window('Floating point input validation', layout)

while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Exit'):
        break
    try:
        in_as_float = float(values['-IN-'])
    except:
        window['-IN-'].update('Debe ingresar un real')
window.close()
