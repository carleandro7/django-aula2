from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [

    path('', views.lista_usuarios, name='lista_usuarios'),
    path('criar/', views.criar_usuario, name='criar_usuario'),
    path('atualizar/<int:pk>/', views.atualizar_usuario, name='atualizar_usuario'),
    path('deletar/<int:pk>/', views.deletar_usuario, name='deletar_usuario'),

    # URL para a página de login
    path('login/', auth_views.LoginView.as_view(template_name='usuarios/login.html'), name='login'),
    
    # URL para fazer logout
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
