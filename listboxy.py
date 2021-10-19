import PySimpleGUI as sg

names = ["John", "Corey", "Adam", "Steve", "Rick", "Thomas"]
empl = [[name, 100] for name in names]


def layout():
    lista = [
        [sg.Listbox(empl, size=(20, 14), key="empleados")],
        [sg.Button("Agregar"), sg.Button("Modificar"), sg.Button("Borrar")],
    ]
    return lista


def crearVentana(registro):
    layout = [[sg.Input(registro[0])], [sg.Input(registro[1])], [sg.Button("Ok")]]
    window = sg.Window("Empleado", layout)
    while True:
        event, values = window.read()
        if event == "Ok":
            window.close()
            return values[0], values[1]


w = sg.Window("", layout())
while True:
    e, v = w.read()
    if e == sg.WIN_CLOSED:
        break
    print(e, v)
    if e == "Agregar":
        nombre, sueldo = crearVentana(["", ""])
        print(nombre, sueldo)
        empl.append([nombre, sueldo])
        w["empleados"].update(empl)
w.close()
