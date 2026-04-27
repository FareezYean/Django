from django.urls import path
from . import views

urlpatterns = [
    # halaman game/ = awal = index
    path('', views.index),
    # halaman game/moba/
    path('moba/', views.moba_view),
    # halaman game/genshin/
    path('genshin/', views.genshin_view),
    # halaman game/dota/
    path('dota/', views.dota_view),
]