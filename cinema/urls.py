from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('cinemaapp.urls')),  # ← подключили маршруты приложения
    path('', include('cinemaapp.urls')),  # подключаем urls из нашего приложения
]

