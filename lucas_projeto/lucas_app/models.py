from django.db import models
from django.contrib.auth.models import AbstractUser


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

from django.contrib.auth.models import AbstractUser
from django.db import models

# Usuário Personalizado
class CustomUser(AbstractUser):

    def __str__(self):
        return self.username
    
from django.db import models
from django.contrib.auth.models import User  # Importa o modelo de usuário padrão ou CustomUser

from django.conf import settings

class Message(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # Relaciona a mensagem ao modelo de usuário configurado
    content = models.TextField()  # Conteúdo da mensagem
    timestamp = models.DateTimeField(auto_now_add=True)  # Data e hora da mensagem

    def __str__(self):
        return f"{self.user.username}: {self.content[:20]}"  # Mostra o nome do usuário e o início da mensagem

