from django.shortcuts import render
from .models import Game

def home(request):
    games = Game.objects.all()
    return render(request, 'home.html', {'games': games})

def search(request):
    query = request.GET.get('query')
    game = Game.objects.filter(name__icontains=query).first()
    if game:
        specifications = game.gamespecifications  # Acesso direto ao atributo relacionado
        return render(request, 'search.html', {'game': game, 'specifications': specifications})
    else:
        return render(request, 'search.html', {'game': None})


