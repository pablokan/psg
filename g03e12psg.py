#1: Ingresar la lluvia caída en milímetros para cada día de la semana. 
#2: Mostrar al final el total de lluvia caída y el nombre del día que más llovió.

import PySimpleGUI as sg

dS = ['lunes', 'martes', 'miércoles', 'jueves', 'viernes', 'sábado', 'domingo']
def layout(): # Define la interfaz grafica
    lista = [[sg.Text(f'{dia}', size=(10, 1)), sg.Input(key=f'entero_mm_{dia}')] for dia in dS]
    lista.append([sg.Button('Ok', bind_return_key=True), sg.Text('', key='salida', size=(30, 1))])
    lista.append([sg.Text('', key='salida2', size=(50, 1))])
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
        mmListInt = [int(x) for x in values.values()]
        maxMM = max(mmListInt)
        print(maxMM)
        total = 0
        diasMasLluviosos = []
        for x in range(7):
            if maxMM == mmListInt[x]:
                diasMasLluviosos.append(dS[x])
            total += mmListInt[x]
        s = f'El total de lluvia caída es {total}'
        if len(diasMasLluviosos) == 1:
            s2 = 'El día más lluvioso fue '
            s2Dias = diasMasLluviosos[0]
        else:
            s2 = 'Los días más lluviosos fueron '
            s2Dias = ", ".join(diasMasLluviosos)
            s2Dias = s2Dias[:s2Dias.rfind(',')] + ' y' + s2Dias[s2Dias.rfind(',')+1:]
        s2 +=  f'{s2Dias}'
        print(diasMasLluviosos)
        window['salida'].update(s)
        window['salida2'].update(s2)

    while True:
        event, values = window.read()
        print(event, values)
        if event in (sg.WIN_CLOSED, 'Quit'): break
        if validate_input(values):
            valid_main()

if __name__ == '__main__':
    w = sg.Window('Title', layout(), location=(2600,330),resizable=True)
    main(w)
    w.close()
