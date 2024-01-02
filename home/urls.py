from django.urls import path

from . import views

app_name = 'home'

urlpatterns = [
    path('', views.home_index, name='home_index'),
    path('category/<slug:slug>/', views.home_index, name='category_filter'),
    path('device/<slug:slug>/', views.device_detail, name='device_detail'),
]
