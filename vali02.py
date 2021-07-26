import PySimpleGUI as sg

"""
    Restrict the characters allowed in an input element to digits and . or -
    Accomplished by removing last character input if not a valid character
"""

layout = [  [sg.Text('Input only floating point numbers')],
            [sg.Input(key='-IN-', enable_events=True)],
            [sg.Button('Exit')]  ]

window = sg.Window('Floating point input validation', layout)

while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Exit'):
        break
    # if last character in input element is invalid, remove it
    if event == '-IN-' and values['-IN-']:
        try:
            in_as_float = float(values['-IN-'])
        except:
            if len(values['-IN-']) == 1 and values['-IN-'][0] == '-':
                continue
            window['-IN-'].update(values['-IN-'][:-1])
window.close()