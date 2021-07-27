import PySimpleGUI as sg
m = ['Jota', 'Eme']
w =sg.Window('', [[sg.Button('Popy')]], size=(400, 400))
e, v = w.read()
if e == 'Popy':
    sg.Popup('\n'.join(m))
w.close()
