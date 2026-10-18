from django.urls import path
from .views import leaderboard

urlpatterns = [
    path('ranking/', leaderboard, name='ranking_clientes'),
]