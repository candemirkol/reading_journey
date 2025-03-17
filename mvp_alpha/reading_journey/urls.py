from django.urls import path
from . import views


app_name = 'reading_journey'

urlpatterns = [
    path('', views.index, name='index'),
    path('archipelago/<int:archipelago_id>/', views.archipelago_detail, name='archipelago_detail'),
    path('island/<int:island_id>/', views.island_detail, name='island_detail'),
]