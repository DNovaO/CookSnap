from django.shortcuts import render
from django.http import JsonResponse
from .tests import buscarIngredientes
import json
import requests
from bs4 import BeautifulSoup

def groceries(request):
    return render(request, 'groceries_template/groceries.html')

def process_ingredients(request):
    if request.method == 'POST':
        try:
            print('hola')
            data = json.loads(request.body)
            ingredients = data.get('ingredients', [])
            
            # Aquí hacemos la búsqueda de recetas
            resultados = buscarIngredientes('https://www.recetasgratis.net/', ingredients)

            recipe_links = []
            if resultados:
                for palabra, links in resultados.items():
                    if links:
                        # Se asume que links contiene una lista de URLs. Si no es así, debes ajustar el código.
                        recipe_links.append({'ingredient': palabra, 'url': links[0]})
            
            return JsonResponse({'status': 'success', 'message': 'Ingredients processed successfully.', 'recipe_links': recipe_links})

        except json.JSONDecodeError:
            return JsonResponse({'status': 'error', 'message': 'Invalid data'}, status=400)

    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=405)

def obtener_links_de_ingrediente(url, ingrediente):
    print(f"Fetching links for ingredient '{ingrediente}' from URL: {url}")
    # Hacer una solicitud HTTP a la página
    response = requests.get(url)
    if response.status_code == 200:
        print(f"Successfully fetched URL: {url}")
        # Usar BeautifulSoup para analizar el HTML de la página
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Buscar todos los enlaces de recetas (esto depende de la estructura de la página)
        links = []
        for link in soup.find_all('a', href=True):
            # Asegúrate de que el enlace contenga el ingrediente
            if ingrediente.lower() in link.text.lower():
                links.append(link['href'])
        
        print(f"Found links for ingredient '{ingrediente}': {links}")
        return links
    else:
        print(f"Failed to fetch URL: {url}, Status code: {response.status_code}")
        return []

def buscarIngredientes(url, ingredientes):
    print(f"Searching for ingredients: {ingredientes} in URL: {url}")
    resultados = {}
    for ingrediente in ingredientes:
        print(f"Searching for ingredient: {ingrediente}")
        links = obtener_links_de_ingrediente(url, ingrediente)
        if links:
            resultados[ingrediente] = [links[0]]  # Solo agregar el primer enlace encontrado
            print(f"Added first link for ingredient '{ingrediente}': {links[0]}")
    print(f"Final search results: {resultados}")
    return resultados