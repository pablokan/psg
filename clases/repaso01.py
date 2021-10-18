import PySimpleGUI as sg

layout = [
    [sg.Text("label1")],
    [sg.Text("label2"), sg.Input(key="label3")],
    [sg.Input(key="label4", enable_events=True)],
    [sg.Button("OK"), sg.Button("Exit")],
]

window = sg.Window(
    "winTitle", layout, location=(2500, 500)
)  # return_keyboard_events=True

while True:
    event, values = window.read()
    if event in [None, "Exit"]:
        break


window.close()
