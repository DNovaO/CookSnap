from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def main_view(request):
    return render(request, 'mainTemplate/mainTemplate.html')

from django.shortcuts import render

def saved_recipes(request):
    
    return render(request, 'saved_recipes_template/saved_recipes.html')


def explore_recipes_view(request):
    return render(request, 'explore_recipes_template/explore_recipes.html')


def groceries(request):
    return render(request, 'groceries_template/groceries.html')

