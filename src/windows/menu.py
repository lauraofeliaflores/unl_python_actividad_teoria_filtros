import PySimpleGUI as sg

def build():
    """
    Construye la ventana del menú del programa
    """
    sg.theme('DarkBrown2')
    layout_column = [
        [sg.Text('¿Qué datos analizamos?',pad=(50, 0), font='Default 20')],
        [sg.Button(button_text='Imagenes', font='Default 10', size=(50, 2), key="-IMAGE-")],
        [sg.Button(button_text='Palabras', font='Default 10',size=(50, 2), key="-PP-")],
        [sg.Button('Salir', font='Default 10', size=(50, 2))]
    ]
    layout = [[[sg.Text( pad =(0,0), key='-EXPAND-')],  # lo que se expande desde arriba
              [sg.Text( pad=(0,0), key='-EXPAND2-'),    # lo que se expande desde la izquierda
               sg.Column(layout_column, vertical_alignment='center', justification='center',  k='-C-')]]]        
    
    window = sg.Window('Actividad 1 -TEORIA-', layout, use_custom_titlebar=True, disable_close=True,resizable=True, element_justification='center').Finalize()
    window['-C-'].expand(True, True, True)
    window['-EXPAND-'].expand(True, True, True)
    window['-EXPAND2-'].expand(True, True, True)
    window.Maximize()
    return window

def build_wind_word():
    sg.theme('DarkBrown2')
    layout_column = [
        [sg.Button(button_text='Marcas de productos con mayor cantidad de alimentos libre de gluten', font='Default 10',size=(50, 2), key="-PLG-")],
        [sg.Button(button_text='Productos de marca Fortuna:', font='Default 10',size=(50, 2), key="-PM-")],
        [sg.Button('Volver', font='Default 10', size=(50, 2))]
    ]
    layout = [[[sg.Text( pad =(0,0), key='-EXPAND3-')],  # lo que se expande desde arriba
              [sg.Text( pad=(0,0), key='-EXPAND4-'),              # lo que se expande desde la izquierda
               sg.Column(layout_column, vertical_alignment='center', justification='center',  k='-C1-')]]]  

    window = sg.Window('Actividad 1 -TEORIA-', layout, use_custom_titlebar=True, disable_close=True,resizable=True, element_justification='center').Finalize()
    window['-C1-'].expand(True, True, True)
    window['-EXPAND3-'].expand(True, True, True)
    window['-EXPAND4-'].expand(True, True, True)
    window.Maximize()
    return window           

def build_wind_image():
    sg.theme('DarkBrown2')
    layout_column = [
        [sg.Button(button_text="Banderas de paises que comienzan con letra A", font='Default 10',size=(50, 2), key="-BAN-")],
        [sg.Button('Volver', font='Default 10', size=(50, 2))]
    ]
    layout = [[[sg.Text( pad =(0,0), key='-EXPAND5-')],  # lo que se expande desde arriba
              [sg.Text( pad=(0,0), key='-EXPAND6-'),              # lo que se expande desde la izquierda
               sg.Column(layout_column, vertical_alignment='center', justification='center',  k='-C3-')]]]  

    window = sg.Window('Actividad 1 -TEORIA-', layout, use_custom_titlebar=True, disable_close=True,resizable=True, element_justification='center').Finalize()
    window['-C3-'].expand(True, True, True)
    window['-EXPAND5-'].expand(True, True, True)
    window['-EXPAND6-'].expand(True, True, True)
    window.Maximize()
    return window 





