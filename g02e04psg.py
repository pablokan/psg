# Pedir el ingreso de 10 números. Contar los mayores de 23.

import PySimpleGUI as sg

layout = [
    [sg.Text("Ingrese 10 números")],
    [sg.Input(size=(5, 1)) for _ in range(5)],
    [sg.Button("Proceso"), sg.Text(key='Salida', size=(3, 1))]
    ]

window = sg.Window("Guía 2 Ej 04", layout)

while True:
    event, values = window.read()
    if event in [None]:
        break
    c = 0
    for i in range(len(values)):
        if not(values[i].isdigit()):
            values[i] = 0
        if int(values[i]) > 23:
            c += 1
    window['Salida'].update(str(c))
    
window.close()
