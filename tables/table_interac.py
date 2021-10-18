import PySimpleGUI as sg
import csv

nombreArchivo = sg.popup_get_file("Seleccione el archivo")

archivo = open(nombreArchivo, "r")
reader = csv.reader(archivo)
cabecera = next(reader)
data = list(reader)
archivo.close()
print(data)
filas = [
    [
        sg.Table(
            values=data, headings=cabecera, change_submits=True, bind_return_key=True
        )
    ]
]

w = sg.Window("Título", filas)  # , return_keyboard_events=True
while True:
    event, values = w.read()
    if event == None:
        break
    print(event, values)
    print(data[values[0][0]])
w.close()
