# MILES
from random import randint
import PySimpleGUI as sg

def layout(): # Define la interfaz grafica
    lista = [
        [
        sg.Text('Número: ', font='any 20'), 
        sg.Input(key='entero_n', font='any 20', size=(4, 1)), 
        sg.Button('Ok', bind_return_key=True), 
        sg.T('B:'),
        sg.I('____', key='bien', size=(4, 1)), 
        sg.T('R:'),
        sg.I('____', key='regular', size=(4, 1)),
        sg.T('M:'),
        sg.I('______', key='mal', size=(6, 1))
        ]
            ]
    lista.insert(0, [sg.Text('Ingrese un número de 4 cifras', size=(30, 1), key='inicio')])
    return lista

def main(window):
    intentos = 0
    def validate_input(values): # Define la validacion de los datos ingresados
        vD = {'entero': int, 'real': float}
        for k, v in values.items():
            tipo = k.split('_')[0]
            if tipo in vD:
                try:
                    i = vD[tipo](v)
                    if i<1000 or i > 9999:
                        return False
                except:
                    window[k].update(value=f'Error: Debe ser un {tipo}')
                    window[k].set_focus()
                    return False
        return True

    def valid_main():
        """Algoritmo Principal Validado"""
        bien = 0
        regular = 0
        a = values["entero_n"]
        for x in range(4):
            if a[x] in n:
                if a[x] == n[x]:
                    bien += 1
                else:
                    regular += 1
        if bien == 4:
            s = f"Acertó! Número: {''.join(n)}. Intentos: {intentos}"
        else:
            s = f"{bien} bien y {regular} regular. Intento #{intentos}"
        s = a + ' -> ' + s
        window.extend_layout(window, [[sg.T(s)]])

    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Quit'): break
        if validate_input(values):
            intentos += 1
            valid_main()

def initComputerNumber():
    c = 0
    n = []
    while c < 4:
        z = randint(0, 9)
        if str(z) not in n:
            n.append(str(z))
            c += 1
    if n[0] == '0':
        x = randint(1, 3)
        n[0], n[x] = n[x], n[0]
    return n


if __name__ == '__main__':
    n = initComputerNumber()
    print(n)
    w = sg.Window('MILES', layout(), location=(2600,330),resizable=True)
    main(w)
    w.close()
