from django.urls import path

from . import views

app_name = 'preventivemaintenance'

urlpatterns = [
    path('preventivemaintenance/<slug:slug>/', views.preventivemaintenance_view, name='preventivemaintenance_view'),
]
