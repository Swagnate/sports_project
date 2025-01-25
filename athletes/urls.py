from django.urls import path
from .views import (
    country_list, country_create, country_edit, country_delete,
    discipline_list, discipline_create, discipline_edit, discipline_delete,
    athlete_list, athlete_create, athlete_edit, athlete_delete
)

urlpatterns = [
    # URL для стран
    path('countries/', country_list, name='country_list'),
    path('countries/create/', country_create, name='country_create'),
    path('countries/edit/<int:pk>/', country_edit, name='country_edit'),
    path('countries/delete/<int:pk>/', country_delete, name='country_delete'),

    # URL для дисциплин
    path('disciplines/', discipline_list, name='discipline_list'),
    path('disciplines/create/', discipline_create, name='discipline_create'),
    path('disciplines/edit/<int:pk>/', discipline_edit, name='discipline_edit'),
    path('disciplines/delete/<int:pk>/', discipline_delete, name='discipline_delete'),

    # URL для участников
    path('athletes/', athlete_list, name='athlete_list'),
    path('athletes/create/', athlete_create, name='athlete_create'),
    path('athletes/edit/<int:pk>/', athlete_edit, name='athlete_edit'),
    path('athletes/delete/<int:pk>/', athlete_delete, name='athlete_delete'),
]