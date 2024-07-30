# djangocrud/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tasks/', include('tasks.urls')),  # Incluye las URLs de la aplicación tasks
    path('', include('tasks.urls')),  # Incluye la URL raíz para la aplicación tasks
]

