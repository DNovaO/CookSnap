from django.shortcuts import render
from django.http import JsonResponse
from .tests import buscarIngredientes
import json
# Create your views here.

def groceries(request):
    return render(request, 'groceries_template/groceries.html')

def process_ingredients(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)  # Leer los datos JSON enviados desde el frontend
            ingredients = data.get('ingredients', [])  # Obtener la lista de ingredientes
            
            # Una vez que atrapa la lista, hace la búsqueda en la página web
            resultados = buscarIngredientes('https://www.recetasgratis.net/Tortilla-busqCate-1.html', ingredients)
            if resultados:
                for palabra, ocurrencias in resultados.items():
                    print(f"La palabra '{palabra}' aparece {ocurrencias} veces en la página.")

            return JsonResponse({'status': 'success', 'message': 'Ingredients processed successfully.'})
        except json.JSONDecodeError:
            return JsonResponse({'status': 'error', 'message': 'Invalid data'}, status=400)
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=405)
