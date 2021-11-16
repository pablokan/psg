import PySimpleGUI as sg

layout1 = [[sg.Button('Ir a pantalla 2', key='pant2')]]

layout2 = [[sg.Text(f'Fila {row}, Columna{col}') for col in range(4)] for row in range(4)]

layout = [[sg.Column(layout1, key='-COL1-'), sg.Column(layout2, visible=False, key='-COL2-')]]

window = sg.Window('Swapping the contents of a window', layout, size=(500, 500))

layout = 1 
while True:
    event, values = window.read()
    if event in (None, 'Exit'):
        break
    if event in 'pant2':
        window[f'-COL{layout}-'].update(visible=False)
        layout = int(event)
        window[f'-COL{layout}-'].update(visible=True)
window.close()
