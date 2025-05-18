from django.urls import path
from . import views

urlpatterns = [
    path('', views.movie_list, name='movie_list'),
    path('movie/<int:movie_id>/', views.movie_detail, name='movie_detail'),
    path('sessions/', views.session_list, name='session_list'),
    path('book/<int:session_id>/', views.book_ticket, name='book_ticket'),
    path('booking-success/', views.booking_success, name='booking_success'),
    path('movie/<int:movie_id>/sessions/', views.movie_sessions, name='movie_sessions'),
]

