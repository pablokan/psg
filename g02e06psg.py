# Preguntar cuántas personas se van a cargar y luego solicitar sus edades,
# mostrando al final la edad promedio.

import PySimpleGUI as sg


def layout():  # Define la interfaz grafica
    # Ejemplo de Pantalla
    lista = [
        [
            sg.Text("Cuántas personas se van a cargar: ", size=(10, 1)),
            sg.Input(key="entero_cantidad"),
        ],
        [sg.Button("Ok", bind_return_key=True), sg.T("", key="msg", size=(30, 1))],
        [sg.Text("", key="salida", size=(30, 1))],
    ]
    return lista


def main(window, promedio):
    def validate_input(values):  # Define la validacion de los datos ingresados
        vD = {"entero": int, "real": float}
        for k, v in values.items():
            tipo = k.split("_")[0]
            if tipo in vD:
                try:
                    vD[tipo](v)
                    window["msg"].update(value="")
                except:
                    window["msg"].update(value=f"Error: Debe ser un {tipo}")
                    window[k].set_focus()
                    return False
        return vD[tipo](v)

    def valid_main(cantidad, promedio):
        if promedio == 0:
            for c in range(cantidad):
                print(values)
                window.extend_layout(
                    window,
                    [
                        [
                            sg.T(f"Edad de la persona {c+1}: ", size=(20, 1)),
                            sg.I(key=f"entero_edad{c+1}"),
                        ]
                    ],
                )
            window.extend_layout(
                window,
                [[sg.Button(f"Obtener promedio", size=(20, 1))]],
            )
        else:
            lista = [int(x) for x in values.values()].pop(0)
            promedio = sum(lista) / cantidad
            print(promedio)
            window["salida"].update(str(promedio))
            return promedio

    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, "Quit"):
            break
        cantidad = validate_input(values)
        if cantidad:
            if valid_main(cantidad, promedio):
                break


if __name__ == "__main__":
    promedio = 0
    w = sg.Window("Title", layout(), resizable=True)
    main(w, promedio)
    w.close()
