from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Página inicial
    path('home/', views.home, name='home'),  # Página Home
    path('search/', views.search, name='search'),  # Pesquisa
    path('register/', views.register, name='register'),  # Cadastro
    path('login/', views.user_login, name='login'),  # Login
    path('logout/', views.user_logout, name='logout'),  # Logout
]
