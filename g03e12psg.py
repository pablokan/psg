#1: Ingresar la lluvia caída en milímetros para cada día de la semana. 
#2: Mostrar al final el total de lluvia caída y el nombre del día que más llovió.

import PySimpleGUI as sg

dS = ['lunes', 'martes', 'miércoles', 'jueves', 'viernes', 'sábado', 'domingo']
def layout(): # Define la interfaz grafica
    lista = [[sg.Text(f'{dia}', size=(10, 1)), sg.Input(key=f'entero_mm_{dia}')] for dia in dS]
    lista.append([sg.Button('Ok', bind_return_key=True), sg.Text('', key='salida', size=(30, 1))])
    lista.insert(0, [sg.Text('Ingresar lluvia caída por día')])
    return lista

def main(window):
    def validate_input(values): # Define la validacion de los datos ingresados
        vD = {'entero': int, 'real': float}
        for k, v in values.items():
            tipo = k.split('_')[0]
            if tipo in vD:
                try:
                    vD[tipo](v)
                except:
                    window[k].update(value=f'Error: Debe ser un {tipo}')
                    window[k].set_focus()
                    return False
        return True

    def valid_main():
        """Algoritmo Principal Validado"""
        total = 0
        for x in range(7):
            total += int(values[f'entero_mm_{dS[x]}'])
        s = f'El total de lluvia caída es {total}'
        window['salida'].update(s)
        # TODO día que más llovió

    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Quit'): break
        if validate_input(values):
            valid_main()

if __name__ == '__main__':
    w = sg.Window('Title', layout(), location=(2600,330),resizable=True)
    main(w)
    w.close()
