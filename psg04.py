import PySimpleGUI as sg

def layout():
    return [[sg.Text('Hi')]]

def main(window):
    event, values = window.read()
    print(event, type(event), values, type(values))

if __name__ == '__main__':
    w = sg.Window('Window Title', layout())
    main(w)
    w.close()
