#from django.test import TestCase
from bs4 import BeautifulSoup
import requests

# Create your tests here.

def buscarIngredientes(url, lista_palabras):
    
    response = requests.get(url) # Solcitud GET a la página web

    if response.status_code == 200: # Solicitud exitosa
        soup = BeautifulSoup(response.content, 'html.parser')   # Parsear el contenido HTML con BeautifulSoup

        texto_web = soup.get_text()

        # Crear un diccionario para almacenar los resultados
        resultados = {palabra: 0 for palabra in lista_palabras}

        for palabra in lista_palabras:
            resultados[palabra] = texto_web.lower().count(palabra.lower())  # Busca los ingredientes
        return resultados
    else:
        print(f"Error al acceder a la página: {response.status_code}")
        return None