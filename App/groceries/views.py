from django.shortcuts import render
from django.http import JsonResponse
from .tests import buscarIngredientes
import json
from django.http import JsonResponse
from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

def groceries(request):
    return render(request, 'groceries_template/groceries.html')

# Cargar modelo GPT-2 y tokenizer
tokenizer = AutoTokenizer.from_pretrained("EleutherAI/gpt-neo-1.3B")
model = AutoModelForCausalLM.from_pretrained("EleutherAI/gpt-neo-1.3B")

def generate_recipe(ingredients):
    # Construir el prompt
    prompt = (
        f"You are a professional chef. Create a detailed, delicious, and unique recipe "
        f"using the following ingredients: {', '.join(ingredients)}. "
        f"Include a catchy recipe title, a brief description, a list of ingredients with quantities, "
        f"and step-by-step cooking instructions. "
        f"Make sure the recipe is coherent and practical for home cooking.\n\n"
        f"Recipe Title:"
    )
    
    # Codificar el prompt
    inputs = tokenizer.encode(prompt, return_tensors="pt")

    # Generar el texto
    output = model.generate(
        inputs,
        max_length=300,
        num_return_sequences=1,
        no_repeat_ngram_size=2,
        pad_token_id=tokenizer.eos_token_id,
    )

    # Decodificar el resultado generado
    generated_text = tokenizer.decode(output[0], skip_special_tokens=True)

    # Extraer la receta eliminando el prompt inicial
    recipe = generated_text[len(prompt):].strip()
    return recipe

def process_ingredients(request):
    if request.method == 'POST':
        # Procesar la solicitud JSON
        data = json.loads(request.body)
        ingredients = [item['food'] for item in data['ingredients']]

        # Generar la receta basada en los ingredientes
        recipe = generate_recipe(ingredients)

        # Responder con solo la receta en JSON
        return JsonResponse({'recipe': recipe})
    
    return JsonResponse({'error': 'Invalid request'}, status=400)
