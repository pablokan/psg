# Determinar cuál es la vocal que aparece con mayor frecuencia.
""" 
frase = "abuobbeeccciauiaiaidjncuicuicucuodkeoqkaok"
vocales = "aeiou"
lista = [frase.count(v) for v in vocales]
for i in range(len(lista)):
    if lista[i] == max(lista):
        print(vocales[i])
"""

import PySimpleGUI as sg


def layout():
    lista = [
        [sg.Text("Ingrese frase: "), sg.Input(key="frase")],
        [sg.Button("Obtener vocal más frecuente", bind_return_key=True)],
        [sg.Text("", key="salida", size=(30, 1))],
        [sg.Button("Quit")],
    ]
    return lista


def main(window):
    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, "Quit"):
            break
        frase = values["frase"]
        vocales = "aeiou"
        lista = [frase.count(v) for v in vocales]
        salida = "Vocales más frecuentes: "
        for i in range(len(lista)):
            if lista[i] == max(lista):
                salida += " " + vocales[i]
        window["salida"].update(salida)


if __name__ == "__main__":
    w = sg.Window("Vocales", layout())
    main(w)
    w.close()
