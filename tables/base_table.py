import PySimpleGUI as sg
import csv

nombreArchivo = sg.popup_get_file("Seleccione el archivo")

archivo = open(nombreArchivo, "r")
reader = csv.reader(archivo)
cabecera = next(reader)
data = list(reader)
archivo.close()

w = sg.Window("Título", [[sg.Table(values=data, headings=cabecera)]])
w.read()
w.close()
