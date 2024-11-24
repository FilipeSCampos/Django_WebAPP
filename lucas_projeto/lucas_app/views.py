from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from .forms import CustomUserCreationForm, CustomAuthenticationForm
from .models import Game
from .models import Game, Message
from .forms import MessageForm
from django.contrib.auth.decorators import login_required

def index(request):
    """Página inicial com opções de login e registro."""
    if request.user.is_authenticated:
        return redirect('home')  # Redireciona para Home se já estiver logado
    return render(request, 'index.html')


@login_required
def home(request):
    games = Game.objects.all()  # Carrega os jogos para o dropdown
    messages = Message.objects.all().order_by('-timestamp')  # Carrega as mensagens mais recentes
    message_form = MessageForm()

    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.user = request.user  # Associa a mensagem ao usuário logado
            message.save()
            return redirect('home')  # Redireciona para limpar o formulário

    context = {
        'games': games,
        'messages': messages,
        'message_form': message_form,
    }
    return render(request, 'home.html', context)

@login_required
def search(request):
    """Página de pesquisa de jogos."""
    query = request.GET.get('query', '').strip()
    if query:
        game = Game.objects.filter(name__icontains=query).first()
        if game:
            specifications = game.gamespecifications
            return render(request, 'search.html', {'game': game, 'specifications': specifications})
    return render(request, 'search.html', {'game': None})

def register(request):
    """Página de registro de novos usuários."""
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})

def user_login(request):
    """Página de login de usuários."""
    if request.method == 'POST':
        form = CustomAuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'login.html', {'form': form})

def user_logout(request):
    """Logout e redireciona para a página inicial."""
    logout(request)
    return redirect('index')
