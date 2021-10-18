import PySimpleGUI as sg
w = sg.Window('Title', [[sg.Button('Click me')]])
t = w.read() # returns a tuple of (event: str, values: dict)
w.close()
print(t)