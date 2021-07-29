# MILES
import PySimpleGUI as sg

def layout(): # Define la interfaz grafica
    lista = [
        [sg.Text('Número: ', size=(10, 1)), sg.Input(key='entero_n', size=(4, 1))], 
        [sg.Button('Ok', bind_return_key=True), sg.Text('', key='salida', size=(30, 1))]   
        ]
    lista.insert(0, [sg.Text('Ingrese un número de 4 cifras', size=(30, 1), key='inicio')])
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
        # Ejemplo
        s = f'El doble de la edad es {int(values["entero_n"])*2}'
        window['salida'].update(s)

    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Quit'): break
        if validate_input(values):
            valid_main()

if __name__ == '__main__':
    w = sg.Window('MILES', layout(), location=(2600,330),resizable=True)
    main(w)
    w.close()
