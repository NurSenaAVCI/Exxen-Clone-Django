from django.urls import path
from .views import *

urlpatterns = [
    path('<slug:profile_slug>/', home_page, name="home_page"),
    path('password/<str:user_username>/', password_change_view, name='password_change_page'),
    path('movie/<slug:profile_slug>/<slug:movie_slug>/', movie_view, name='movie_page'),
]