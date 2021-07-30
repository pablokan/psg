import PySimpleGUI as sg

layout = [[sg.Text('My Text Element',
                font='Helvetica 20 bold underline',
                text_color='#FF0000',
                background_color='white',
                justification='center',
                key='-text-',
                border_width=20,
                tooltip='This is a text element'
                )]]

w = sg.Window('Window Title', layout)
w.read()
w.close()
