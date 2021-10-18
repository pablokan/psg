import PySimpleGUI as sg

def layout(d, c):
    lista = [[sg.Text(f'{d} {x}'), sg.InputText(key=f'{d}{x}')] for x in range(c)]
    lista.append([sg.Text(size=(40,1), key='output')])
    lista.append([sg.Button('Show'), sg.Button('Exit')])
    return lista

def main(window, d):                                                
    while True:
        event, values = window.read()
        print(event, type(event), values, type(values))
        if event in (sg.WINDOW_CLOSED, 'Exit'): break
        salida = 'Salida: ' + values[f'{d}1']
        window['output'].update(salida)


if __name__ == '__main__':
    dato = 'Dato'
    w = sg.Window('Window Title', layout(dato, 3))
    main(w, dato)
    w.close()
