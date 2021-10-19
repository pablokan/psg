import PySimpleGUI as sg

names = ["John", "Corey", "Adam", "Steve", "Rick", "Thomas"]
empl = [[name, 100] for name in names]
empl.sort()


def layout():
    lista = [
        [sg.Text("Nombre y Sueldo")],
        [sg.Listbox(empl, size=(20, 14), key="empleados")],
        [sg.Button("Agregar"), sg.Button("Modificar"), sg.Button("Borrar")],
    ]
    return lista


def crearVentana(msg, registro):
    layout = [[sg.Input(registro[0])], [sg.Input(registro[1])], [sg.Button("Ok")]]
    window = sg.Window(f"{msg} Empleado", layout)
    while True:
        event, values = window.read()
        if event == "Ok":
            window.close()
            return values[0], values[1]


w = sg.Window("Listado de Empleados", layout())
while True:
    e, v = w.read()
    if e == sg.WIN_CLOSED:
        break
    print(e, v)
    if e == "Agregar":
        nombre, sueldo = crearVentana(e, ["", ""])
        empl.append([nombre, sueldo])
        empl.sort()
    elif e == "Modificar":
        selElement = v["empleados"][0]
        empl.remove(selElement)
        nombre, sueldo = crearVentana(e, selElement)
        empl.append([nombre, sueldo])
        empl.sort()
    elif e == "Borrar":
        selElement = v["empleados"][0]
        empl.remove(selElement)

    w["empleados"].update(empl)

w.close()
