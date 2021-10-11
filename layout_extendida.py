import PySimpleGUI as sg


def layout():  # Define la interfaz grafica
    # Ejemplo de Pantalla
    lista = [
        [sg.Text("Nombre: ", size=(10, 1)), sg.Input(key="nombre")],
        [sg.Text("Vehículo: ", size=(10, 1)), sg.Input(key="vehículo")],
    ]
    lista.append([sg.Button("Más vehículos?")])
    return lista


def main(window):
    c = 0
    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, "Quit"):
            break
        print(event, values)
        if event == "Más vehículos?":
            c += 1
            window.extend_layout(
                window,
                [
                    [
                        sg.T(f"Vehículo adicional {c}: ", size=(20, 1)),
                        sg.I(key=f"vehículo{c}"),
                    ]
                ],
            )


if __name__ == "__main__":
    w = sg.Window("Title", layout(), resizable=True)
    main(w)
    w.close()
