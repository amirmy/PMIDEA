from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('buy/', include('buy.urls', namespace='buy')),
    path('preventivemaintenance/', include('preventivemaintenance.urls', namespace='preventivemaintenance')),
    path('', include('home.urls', namespace='home')),
]
