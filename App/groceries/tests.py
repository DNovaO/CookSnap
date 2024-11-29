#from django.test import TestCase
from bs4 import BeautifulSoup
import requests

# Create your tests here.

def buscarIngredientes(url, lista_palabras):
    
    response = requests.get(url) # Solcitud GET a la página web

    if response.status_code == 200: # Solicitud exitosa
        soup = BeautifulSoup(response.content, 'html.parser')   # Parsear el contenido HTML con BeautifulSoup

        texto_web = soup.get_text() # Obteniendo el texto de la página web

        # Crear un diccionario para almacenar los resultados
        resultados = {palabra: 0 for palabra in lista_palabras}

        for palabra in lista_palabras:
            resultados[palabra] = texto_web.lower().count(palabra.lower())  # Busca los ingredientes
        return resultados
    else:
        print(f"Error al acceder a la página: {response.status_code}")
        return None
    
def getLinks():
    url = 'https://www.recetasgratis.net/Tortilla-busqCate-1.html'
    recetas = []
    response = requests.get(url) # Solcitud GET a la página web
    if response.status_code == 200: # Solicitud exitosa
        soup = BeautifulSoup(response.content, 'html.parser')   # Parsear el contenido HTML con BeautifulSoup
        # Salvando títulos e hipervínculos
        for element in soup.find_all('a'):
            nombre = element.get_text(strip=True)
            href = element.get('href')
            if href:
                full_url = href if href.startswith('http') else url + href
                recetas.append({'nombre': nombre, 'url': full_url})
    else:
        print(f"Error al acceder a la página: {response.status_code}")
        return 
    linksFiltrados = [element for element in recetas if element['nombre'].startswith('Receta')]
    return linksFiltrados
    
def getRecipes(diccionario, ingredientes):
    ingredientesNecesarios = []
    for element in diccionario:
        url = element['url']
        response = requests.get(url)    # Buscará en todas las páginas recolectadas
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            # Buscando los ingredientes
            for element in soup.find_all('li'):     # Encuentra los ingredientes de la página actual
                if 'class' in element.attrs:
                    nombre = element.get_text(strip=True)
                    ingredientesNecesarios.append(nombre)
            # Verificar si el cliente puede preparar la receta
            resultado, porcentaje = canPrepareRecipe(ingredientesNecesarios, ingredientes)
            if resultado:
                print(f"¡Puedes preparar la receta! Coincidencia: {porcentaje:.2%}")
            else:
                print(f"No puedes preparar la receta. Coincidencia: {porcentaje:.2%}")

def canPrepareRecipe(receta, cliente, umbral=0.8):
    """
    Determina si el cliente puede preparar la receta con sus ingredientes.
    
    :param ingredientes_receta: Lista de ingredientes necesarios para la receta.
    :param ingredientes_cliente: Lista de ingredientes que tiene el cliente.
    :param umbral: Porcentaje mínimo de coincidencia para considerar aceptable (por defecto 80%).
    :return: Booleano indicando si puede preparar la receta y porcentaje de coincidencia.
    """
    # Convertir listas en conjuntos para calcular intersección y coincidencias
    ingredientes_necesarios = set(receta)
    ingredientes_disponibles = set(cliente)

    if ingredientes_necesarios:
        print("simón")
    
    # Ingredientes en común
    coincidencias = ingredientes_necesarios.intersection(ingredientes_disponibles)
    porcentaje_coincidencia = len(coincidencias) / len(ingredientes_necesarios)
    
    # Determinar si alcanza el umbral
    aceptable = porcentaje_coincidencia >= umbral
    
    return aceptable, porcentaje_coincidencia


print("Ejecutando la función 'getLinks()' ...")    
recetas = getLinks()

for element in recetas:
    print(f"Nombre: {element['nombre']}, URL: {element['url']}")
# ingredientes = ['acelga', 'zanahoria', 'cebolla', 'ajo', 'pimienta']
# getRecipes(recetas, ingredientes)


# def test():
#     url = 'https://www.recetasgratis.net/receta-de-tortilla-de-acelga-y-zanahoria-77695.html'
#     response = requests.get(url) # Solcitud GET a la página web

#     if response.status_code == 200: # Solicitud exitosa
#         soup = BeautifulSoup(response.content, 'html.parser')
#         with open("test.txt", "w", encoding="utf-8") as file:
#             file.write(soup.prettify())
#     print("Archivo exportado como archivo.txt")

# test()