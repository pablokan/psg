import PySimpleGUI as sg
import csv

nombreArchivo = sg.popup_get_file("Seleccione el archivo")

archivo = open(nombreArchivo, "r")
reader = csv.reader(archivo)
cabecera = next(reader)
data = list(reader)
archivo.close()

filas = [[sg.Table(values=data, headings=cabecera)]]

w = sg.Window("Título", filas)
w.read()
w.close()
