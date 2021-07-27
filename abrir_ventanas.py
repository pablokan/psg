import PySimpleGUI as sg

def layout(): # Define la interfaz grafica
    # Ejemplo de Pantalla
    lista = [
        [sg.Button('Abrir otra ventana', key='abrir', bind_return_key=True)]        
        ]
    return lista

def main(window):
    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Quit'): break
        print(event, values)
        if event == 'abrir':
            sg.Popup('Ventana abierta')
            otraV = sg.Window("Other Window", [[sg.Text("Cualquiera mente")]])
            otraV.read()
            
if __name__ == '__main__':
    w = sg.Window('Title', layout(), location=(2600,330))
    main(w)
    w.close()
