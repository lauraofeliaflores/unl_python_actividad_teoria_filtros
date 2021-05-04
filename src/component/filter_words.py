import PySimpleGUI as sg
from src.windows import menu
import json
import os
import os.path as path
import csv
from itertools import groupby
from collections import Counter

def write_json(data,  json_word):
    """
        Función para generar el JSON 
    """
    with open(json_word,'w') as f:
        json.dump(data, f, indent=4)

def save_info_word(filtered_file, json_word):
    with open(json_word,encoding="utf8") as json_file:
        data = json.load(json_file)
        write_json(data, json_word)

def create_file_words(filtered_file, json_word):
    """
        Función para almacenar los datos en el JSON.
    """
    words = open(json_word, 'w')
    json.dump(filtered_file,words)
    words.close()

def open_file():
    """
        Función para abrir y leer el archivo flags_iso.csv
    """
    file_csv = open("C:/Proyectos/proyectosPython/archivosPY/PySimpleGUI/entrega/actividadTeoria/alimentos-libres-de-gluten.csv", "r", encoding="utf8")
    csvreader = csv.reader(file_csv, delimiter=',')
    return csvreader

def filter_brand_food(file_words):
    """
    Función que ordena y filtra las 10 marca que tienen mas productos libres de gluten.
    """
    _header = next(file_words)
    
    def projection(val):
        """
            Funcion que me convierte un string en mayuscula y lo retorna.
        """
        return val[0].upper()
        
    def count_brand(var):
        """
            Función que me retorna la longitud. 
        """
        return len(var)

    x_sorted = sorted(file_words, key=projection)
    x_grouped = [list(it) for k, it in groupby(x_sorted, projection)] 
    x_sorted2 = sorted(x_grouped, key=count_brand, reverse=True)
    x_sorted3 = x_sorted2[:10]
    new = []
    for i in x_sorted3:
        #print(f'{i[0][0]} {len(i)}')
        new.append({"marca": i[0][0] , "cantidad de productos":len(i)})
    return new 

def save_to_json(filtered_file, json_word):
    """
        Función para crear un archivo JSON y guardar la informacion filtrada.
    """
    if not path.exists(json_word):
        create_file_words(filtered_file, json_word)
    else:
        save_info_word(filtered_file, json_word) 
     
def filter_brand(file_words):
    """
        Función que filtra los productos de marca Fortuna y los gurda en un una lista 
        de diccionarios.
    """
    _header = next(file_words)
    list_brand = filter(lambda x : x[0] == 'Fortuna', file_words)
    new = []
    for elem in list_brand:
        #print(f"{header[0]}: {elem[0]}\n{header[2]}:{elem[2]}")
        new.append({"marca": elem[0], "denominacion": elem[2]})
    return new    

def loop():
    """
    Loop de la ventana de menú que capta los eventos al apretar las opciones
    """
    window  = menu.build_wind_word()
    event, _values = window.read()
    while True:
        if event in (sg.WIN_CLOSED, 'Volver'):
            window.close()
        if event in (sg.Button, '-PLG-'):
            file_words = open_file()
            filtered_file = filter_brand_food(file_words)
            save_to_json(filtered_file, json_word='words.json')
        if event in (sg.Button, '-PM-'):
            file_words = open_file()
            filtered_file_brand = filter_brand(file_words)
            save_to_json(filtered_file_brand, json_word='brand.json')
        return window          

def start():
    """
    Lanza la ejecución de la ventana del menú
    """
    window_new_filter_word = loop()
    window_new_filter_word.close()

   