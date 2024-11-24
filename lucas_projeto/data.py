import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'lucas_projeto.settings')
application = get_wsgi_application()

from lucas_app.models import Game, GameSpecifications

import csv

csv_file_path = r"C:\Users\filip\Desktop\ADS\Django_WebAPP\lucas_projeto\output.csv"

with open(csv_file_path, "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        # Cria ou obtém o jogo pelo nome
        game_name = row["name"]
        game, created = Game.objects.get_or_create(name=game_name)
        
        # Cria as especificações associadas ao jogo
        if created:  # Só cria especificações se o jogo foi criado
            GameSpecifications.objects.create(
                game=game,  # Associa o jogo à especificação
                memory=row["Memory:"],
                graphics_card=row["Graphics Card:"],
                cpu=row["CPU:"],
                file_size=row["File Size:"],
                os=row["OS:"],
            )
        else:
            print(f"Especificações já existem ou o jogo {game_name} já foi adicionado.")
