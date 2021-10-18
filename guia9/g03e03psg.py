#1: Almacenar en dos listas paralelas, nombres y sexos de 8 personas. 
#2: Recorrerlas y mostrar los nombres de las mujeres. 

import PySimpleGUI as sg

def layout(): # Define la interfaz grafica
    # Ejemplo de Pantalla
    lista = [
        [sg.Text(f'Nombre #{x}: ', size=(10, 1)), sg.Input(key=f'nombre_{x}'), 
        sg.Radio('Mujer', key=f'mujer_{x}', group_id=f'Sexo_{x}'), 
        sg.Radio('Hombre', key=f'hombre_{x}', group_id=f'Sexo_{x}')]
        for x in range(1, 9)
        ]
    lista.append([sg.Button('Ok', bind_return_key=True)])    
    return lista

def main(window):
    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Quit'): break
        mujeres = []
        for x in range(1, 9): # copilot me sugirió las dos líneas siguientes
            if values[f'mujer_{x}']:
                mujeres.append(values[f'nombre_{x}'])
        sg.Popup('Nombres de mujeres en la lista', '\n'.join(mujeres), title='Mujeres')
if __name__ == '__main__':
    w = sg.Window('Title', layout(), location=(2600,330),resizable=True)
    main(w)
    w.close()
