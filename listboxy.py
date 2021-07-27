import PySimpleGUI as sg

names = ['John', 'Corey', 'Adam', 'Steve', 'Rick', 'Thomas']

def layout():
    lista = [
    [sg.Listbox(names, size=(20, 4), enable_events=True, key='-LIST-')],
    [sg.Button('Ok')]
    ]
    return lista

w = sg.Window('', layout())
e, v = w.read()
print(e, v)
w.close()
