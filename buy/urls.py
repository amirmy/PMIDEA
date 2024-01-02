from django.urls import path

from . import views

app_name = 'buy'

urlpatterns = [
    path('buy/<slug:slug>/', views.buy_device, name='buy_view'),
    path('buy/create_dynamic_buy/<slug:slug>', views.create_buy, name='create_buy'),

]
