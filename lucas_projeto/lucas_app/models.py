from django.db import models

class Game(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class GameSpecifications(models.Model):
    game = models.OneToOneField(Game, on_delete=models.CASCADE)
    memory = models.CharField(max_length=50)
    graphics_card = models.CharField(max_length=255)
    cpu = models.CharField(max_length=255)
    file_size = models.CharField(max_length=50)
    os = models.CharField(max_length=50)

    def __str__(self):
        return f"Specifications for {self.game.name}"

