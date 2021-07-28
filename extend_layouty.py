import PySimpleGUI as sg

def layout(): # Define la interfaz grafica
    # Ejemplo de Pantalla
    global lista
    lista = [
        [sg.Text('Nombre: ', size=(10, 1)), sg.Input(key='nombre')], 
        [sg.Text('Edad: ', size=(10, 1)), sg.Input(key='edad')], 
        ]
    lista.append([sg.Button('Insert', bind_return_key=True)])    
    return lista

def main(window):
    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Quit'): break
        print(event, values)
        if event == 'Insert':
            window.extend_layout(window, [[sg.T('Sexo: ', size=(10, 1)), sg.I(key='sexo')]])

        
if __name__ == '__main__':
    w = sg.Window('Title', layout(), location=(2600,330),resizable=True)
    main(w)
    w.close()
