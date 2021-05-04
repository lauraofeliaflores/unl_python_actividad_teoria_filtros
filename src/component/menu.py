import PySimpleGUI as sg
from src.windows import menu
from src.component import filter_words, filter_image

def loop():
    """
    Loop de la ventana de menú que capta los eventos al apretar las opciones
    """
    window = menu.build()
    while True:
        event, _values = window.read()
        if event in (sg.WIN_CLOSED, 'Salir'):
            break
        elif  event in (sg.Button, '-IMAGE-'):
            filter_image.start()
            #sg.popup('datos de imagen!')
        elif event in (sg.Button, '-PP-'):
            #sg.popup("datos de palabras")
            filter_words.start()

    return window

def start():
    """
    Lanza la ejecución de la ventana del menú
    """
    window = loop()
    window.close()

