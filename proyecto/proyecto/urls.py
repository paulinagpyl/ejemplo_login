# proyecto/urls.py

from django.contrib import admin
from django.urls import path
from aplicacion import views  # Importa las vistas de la aplicación

urlpatterns = [
    path('admin/', admin.site.urls),  # URL para el panel de administración
    path('', views.index, name='index'),  # Página principal
    path('login/', views.user_login, name='login'),  # Vista de login
    path('logout/', views.user_logout, name='logout'),  # Vista de logout
]
