from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('login/', views.user_login, name="login"),
    path('register/', views.user_register, name="register"),
    path('dashboard/<int:user_id>/', views.user_dashboard, name="dashboard"),
    path('editdashboard/<int:user_id>/', views.edit_dashboard, name="edit_dashboard"),
    path('logout', views.logout, name="logout"),

]
