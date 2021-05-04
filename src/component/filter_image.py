import PySimpleGUI as sg
from src.windows import menu
import json
import os
import os.path as path
import csv
import requests

def open_file():
    """
        Función para abrir y leer el archivo flags_iso.csv
    """
    file_csv = open("C:/Proyectos/proyectosPython/archivosPY/PySimpleGUI/entrega/actividadTeoria/flags_iso.csv", "r", encoding="utf8")
    csvreader = csv.reader(file_csv, delimiter=',')
    return csvreader

def filter_images_of_flags(file_image):
    """
        Función para filtrar del iterable file_image los paises que comienzan con el string "A"
    """
    _header = next(file_image)

    array_blags = filter(lambda x: x[0][0].startswith("A") ,file_image)
    new = []
    for elem in array_blags:
        new.append({"país": elem[0] , "url":elem[3]})
    return  new

def write_json(data,  json_image):
    """
    Función para generar el JSON 
    """
    with open(json_image,'w') as f:
        json.dump(data, f, indent=4)

def create_file_image(filtered_file_image, json_image):
    """
        Función para almacenar los datos en el JSON.
    """
    image = open(json_image, 'w')
    json.dump(filtered_file_image,image)
    image.close() 

def save_info_image(filtered_file_image, json_image):
    """
    Función para guardar UN JSON.
    """
    with open(json_image) as json_file:
        data = json.load(json_file)
        write_json(data, json_image) 

def save_image(items):
    """
      Esta función crea una carpera con las imagenes de las banderas de los paises
      con nombres que comienzan con "A"
    """
    for x in range(0,11):
      image = requests.get(items[x]['url'])
      flag = items[x]['pa\u00eds']
      with open(f'C:/Proyectos/proyectosPython/archivosPY/PySimpleGUI/entrega/actividadTeoria/image/{flag}.jpg', 'wb') as f:
          f.write(image.content)

def save_to_json(filtered_file_image, json_image):
    """
        Función para crear un archivo JSON y guardar la informacion filtrada.
    """
    if not path.exists(json_image):
        create_file_image(filtered_file_image, json_image)
    else:
        save_info_image(filtered_file_image, json_image) 
   
def loop():
    """
    Loop de la ventana de menú que capta los eventos al apretar las opciones
    """
    window  = menu.build_wind_image()
    event, _values = window.read()
    while True:
        if event in (sg.WIN_CLOSED, 'Volver'):
            window.close()
        if event in (sg.Button, '-BAN-'):
            file_image = open_file()
            filtered_file_image = filter_images_of_flags(file_image)
            save_to_json(filtered_file_image, json_image='image.json')
            save_image(filtered_file_image)

        return window          

def start():
    """
    Lanza la ejecución de la ventana del menú
    """
    window_new_filter_image = loop()
    window_new_filter_image.close()