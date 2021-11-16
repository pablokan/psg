
import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import  ColorChooserButton, popup_get_date, popup_menu , popup, theme_button_color, datetime  
import pathlib


#Menu principal
ahora= datetime.datetime.now()

layout = [   
        [sg.Button(ahora.strftime('La Fecha de hoy es  ''%d/%m/%y' '    La Hora Acutal es     ' '%H:%M         '    'Acceda al Calendario'))],                   
        [sg.Button('Contactos',button_color='blue')],
        [sg.Button('Calculadora',button_color='orange')],
        [sg.Button('Bitacora del viaje',button_color='green')],
        [sg.Button('Salir',button_color='red')],
        
        ]


principal = sg.Window('AGENDA INTERACTIVA PARA EL VIAJERO',font=100, default_button_element_size=(40,6), auto_size_buttons=False, grab_anywhere=False)
principal.Layout(layout)






while True:
     
     #Accediendo al Modulo de Calendario
        boton, valor = principal.Read()                          
        
                   
        if boton == ahora.strftime('La Fecha de hoy es  ''%d/%m/%y' '    La Hora Acutal es     ' '%H:%M         '    'Acceda al Calendario'):
            
            
            layout = [
                
                [sg.popup_get_date(no_titlebar=False,title='CALENDARIO')]
            ]
        
        
             
        
        #Accediendo al Modulo de Contactos         
        elif boton == 'Contactos':        
            
            datos = [['Emergencias/Emergency................', 911]]
            layout =[   [sg.Text('APELLIDO Y NOMBRE                   TELEFONO',font=(20),background_color='green')],
                        [sg.Listbox(values=datos,font=40, size=(30,10), key='CONTACTOS',background_color='pink', enable_events=True)],
                        [
                        sg.Button('Agregar',font = (15)),
                        sg.Button('Modificar',font = (15)),
                        sg.Button('Eliminar',font = (15))
                        ],  
                    ]

            window = sg.Window('AGENDA DE CONTACTOS', layout,background_color='blue' )



            
            
            
            
            while True:                  
                boton, valor = window.read()
                
                if valor == sg.WIN_CLOSED:
                    break
                
                
                if valor['CONTACTOS']:
                    nombre=valor['CONTACTOS'][0][0]
                    telefono=valor['CONTACTOS'][0][1]
                    pos=datos.index([nombre,telefono])
                    
                if valor['CONTACTOS'] and boton=='Modificar':
                    layout2=[
                    [sg.Text('Apellido y Nombre'),sg.Input(nombre,key='Nombres')],
                    [sg.Text('Numero Telefonico'),sg.Input(telefono,key='Telefonos')],
                    [sg.Button('Guardar',font = (15))]
                    ]
                    window2=sg.Window('Modificar',layout2)
                    boton,valor = window2.read()
                    if boton=='Guardar':
                        datos.pop(pos)
                        datos.insert(pos,[valor['Nombres'],valor['Telefonos']])
                        window2.close()
                        window['CONTACTOS'].Update(datos)
                if boton=='Eliminar' and valor['CONTACTOS']:
                    datos.pop(pos)
                    window['CONTACTOS'].Update(datos)
                if boton=='Agregar':
                    layout3=[
                    [sg.Text('Apellido y Nombre'),sg.Input(key='Nombres')],
                    [sg.Text('Numero Telefonico'),sg.Input(key='Telefonos')],
                    [sg.Button('Guardar',font = (15))]
                    ]
                    window3=sg.Window('Modificar',layout3)
                    boton,valor = window3.read()
                    if boton=='Guardar':
                        datos.append([valor['Nombres'],valor['Telefonos']])
                        window3.close()
                        window['CONTACTOS'].Update(datos) 
                        
           
                
        
                


        #Accediendo al Modulo Bitacora de Viaje
        if boton == 'Bitacora del viaje':         
        

            menu_layout = [['Archivo', ['Nuevo', 'Abrir', 'Guardar', 'Guardar Como']],
                        ]

            layout = [[sg.Menu(menu_layout)],
                    [sg.Text('Esta es una nueva bitacora, por favor asigne un nombre desde el menu Guardar Como',background_color='green', font=('Arial', 40), size=(60, 3), key='INFORMACION')],
                    [sg.Multiline(font=('Arial', 20), size=(5, 10), key='CUERPO')]]

            window = sg.Window('Bitacora del viaje', layout=layout, margins=(0, 0), resizable=True, return_keyboard_events=True, finalize=True)
            window.maximize()
            window['CUERPO'].expand(expand_x=True, expand_y=True)

            def new_file():
                window['CUERPO'].update(value='')
                window['INFORMACION'].update(value='Esta es una nueva bitacora, por favor asigne un nombre desde el menu Guardar Como') 
                return file

            def open_file():
                filename = sg.popup_get_file('Abrir', no_window=True)
                if filename:
                    file = pathlib.Path(filename)
                    window['CUERPO'].update(value=file.read_text())
                    window['INFORMACION'].update(value=file.absolute())
                    return file

            def save_file(file):
                if file:
                    file.write_text(values.get('CUERPO'))
                else:
                    save_file_as()

            def save_file_as():
                filename = sg.popup_get_file('Guardar Como', save_as=True, no_window=True)
                if filename:
                    file = pathlib.Path(filename)
                    file.write_text(values.get('CUERPO'))
                    window['INFORMACION'].update(value=file.absolute())
                    return file               
                    
        

    
            while True:
                event, values = window.read()
                if event in('Exit', None):
                    break
                if event in ('Nuevo', 'n:78'):
                    file = new_file()
                if event in ('Abrir', 'o:79'):
                    file = open_file()
                if event in ('Guardar', 's:83'):
                    save_file(file)
                if event in ('Guardar Como',):
                    file = save_file_as()   
            
            #Accediendo al Módulo Calculadora
        elif boton == 'Calculadora':
        

            layout = [[sg.Txt(''  * 500)],                      
                    [sg.Text('', size=(0, 1), font=('arial', 100), text_color='black', key='input')],
                    [sg.Txt(''  * 500)],
                    [sg.Button('Limpiar',button_color='orange',font=50), sg.Button('Retroceso',button_color='pink',font=50),sg.Button('Divisa',button_color='black',font=50), sg.Button('Millas a Km',button_color='blue',font=50)],
                    [sg.Button('7',font=20), sg.Button('8',font=20), sg.Button('9',font=20), sg.Button('+',font=30)],
                    [sg.Button('4',font=20), sg.Button('5',font=20), sg.Button('6',font=20), sg.Button('-',font=30)],
                    [sg.Button('1',font=20), sg.Button('2',font=20), sg.Button('3',font=20), sg.Button('*',font=30)],
                    [sg.Button('0',font=20), sg.Button('.',font=20), sg.Button('=',font=100,button_color='green'), sg.Button('/',font=30)],
                    ]
            
            
            calcu= sg.Window('calculadora', default_button_element_size=(15, 5), auto_size_buttons=False, grab_anywhere=False)
            calcu.Layout(layout)
            

            mensaje=''
            ecuacion = ''
            errorDeOperaciones=  ['+','-','*','/']


            while True:
                boton, valor = calcu.Read()                          
            
                  
                
                if boton == 'Limpiar':
                    ecuacion = ''
                    calcu.find_element('input').Update(ecuacion)
                elif boton == 'Retroceso':
                    ecuacion = ecuacion[:-1]
                    calcu.find_element('input').Update(ecuacion)
                elif len(ecuacion) == 15:
                    pass
                elif str(boton) in '0123456789+-./*':
                    ecuacion += str(boton)
                    calcu.find_element('input').Update(ecuacion) 
            
                #Convertidor de Divisa Para obtener Dolares
                elif boton == 'Divisa':
                    sg.change_look_and_feel('black')

                    layout = [ [sg.Text('Tengo en Pesos',font=100), sg.Input(key='convertidor',font=40, do_not_clear=False, size=(8,1)),sg.Text('cotizacion',font=40),sg.Input(key='cotizacion',font=100, do_not_clear=False,size=(8,1))],
                    [sg.Text('Con mis',font=100),sg.Text(size=(10,1),font=40, key='salida d'),
                        sg.Text('Pesos puedo obtener = ',justification='left',font=100),
                        sg.Text(size=(10,1), key='salida p',font=40),
                        sg.Text('Dolares',font=100)],
                    [sg.Button('Convertir',font=200, bind_return_key=True), sg.Button('Salir',font=200)]  ]

                    window = sg.Window('OBTENCION DE DOLARES', layout,font=100,background_color='green')

                    while True:             
                        event, values = window.read()
                        if event in (None, 'Salir'):
                            break
                        window['salida d'].Update(values['convertidor']),
                        window['salida p'].Update(float(values['convertidor'])/float(values['cotizacion'])),
                        
                    window.close()

                    #Convertidor de Millas a Kilometros (para viajar a EEUU) 
                elif boton == 'Millas a Km':

                    layout = [ [sg.Text('Ingrese cantidad de Millas',font=100), sg.Input(key='convertidor',font=100, do_not_clear=False, size=(10,1))],
                    [sg.Text(size=(10,1), key='salida k'),
                        sg.Text('Millas equivalen a: ',font=100),
                        sg.Text(size=(5,1), key='salida mi'),
                        sg.Text('Kilometros',font=100)],
                    [sg.Button('Convertir',font=100, bind_return_key=True), sg.Button('Salir',font=100)]  ]

                    window = sg.Window('CONVERTIR MILLA A KILOMETROS', layout,font=100,background_color='red')

                    while True:             
                        event, values = window.read()
                        if event in (None, 'Salir'):
                            break
                        window['salida k'].Update(values['convertidor'])
                        window['salida mi'].Update(float(values['convertidor'])/0.6214)
                    window.close()

                elif boton == '=':

                    for i in errorDeOperaciones :  
                        if '*' == ecuacion[0] or '/' == ecuacion[0]  or i == ecuacion[-1]:   
                            Responde = "Error" 
                            break
                        elif '/0' in ecuacion or '*/' in ecuacion or '/*' in ecuacion :
                            Responde= "Error div '0' no existe" 
                            break
                
                    else :
                        Responde = str("%0.2f" %(eval(ecuacion)))                         
                        if '.0' in Responde:
                            Responde = str(int(float(Responde)));                          
                    calcu.find_element('input').Update(Responde)                         
                    ecuacion = Responde
                    
                else:
                     boton is None 
                     break            
        
        else:
            boton is None                          
            break

