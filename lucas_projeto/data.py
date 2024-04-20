import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'lucas_projeto.settings')
application = get_wsgi_application()

from lucas_app.models import Game, GameSpecifications

import csv

csv_file_path = r"C:\Users\FilipeCampos\Desktop\projeto_luketa_ceub\lucas_projeto\output.csv"

with open(csv_file_path, "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        game_name = row["name"]
        game, created = Game.objects.get_or_create(name=game_name)
        if created:
            specifications = GameSpecifications.objects.create(
                memory=row["Memory:"],
                graphics_card=row["Graphics Card:"],
                cpu=row["CPU:"],
                file_size=row["File Size:"],
                os=row["OS:"],
            )
            game.specifications = specifications
            game.save()
