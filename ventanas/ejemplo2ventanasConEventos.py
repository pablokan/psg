# Base para dos ventanas, ambas abiertas y con eventos.

import PySimpleGUI as sg


def contenidoVentanaUno():
    filas = [
        [sg.Text("Menú de Opciones", size=(30, 1))],
        [sg.Button("Opción 1")],
        [sg.Button("Salir")],
        [sg.T(key="msg", size=(30, 1))],
    ]
    return filas


def contenidoVentanaDos():
    filas = [[sg.Text(f"texto de la segunda ventana", size=(30, 1))]]
    filas.append(
        [sg.Button("Ok", bind_return_key=True), sg.T("", key="salida", size=(30, 1))]
    )
    return filas


def main(firstWindow):
    def wLoop(window, fAction, msg):
        while True:
            event, values = window.read()
            if event in (sg.WIN_CLOSED, "Salir"):
                break
            fAction(window, values)

    def action2(secondWindow, values2):
        print(values2)
        secondWindow["salida"].update("apreté el botón OK")

    def action1(firstWindow, values1):
        firstWindow["msg"].update("Abrí la segunda ventana")
        secondWindow = sg.Window("Ventana Dos", layout=contenidoVentanaDos())
        wLoop(secondWindow, action2, "salida")

    wLoop(firstWindow, action1, "msg")


if __name__ == "__main__":
    ventanaPrincipal = sg.Window("Ventana Uno", contenidoVentanaUno())
    main(ventanaPrincipal)
    ventanaPrincipal.close()
