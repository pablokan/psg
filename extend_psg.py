import PySimpleGUI as sg
import PySimpleGUI as sg

class InputK(sg.Input):
        def __init__(self, **kwargs):
            super().__init__(**kwargs)
            #print(kwargs)
        
        def foo(self):
            return "foooooo"

q = InputK(key='-IN-')
#print('q:', q.foo())
w = sg.Window('', [[q], [sg.Button('Nada')]], size=(200, 100))
event, values = w.read()
print(event, values['-IN-'])
w.close()
