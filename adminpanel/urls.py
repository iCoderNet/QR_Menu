from django.urls import path
from .views import *

urlpatterns = [
    path('', admin_dashboard, name='admin-dashboard'),
    path('login/', admin_login, name='admin-login'),
    path('logout/', admin_logout, name='admin-logout'),
    path('profile/', admin_profile, name='admin-profile'),
    path('settings/', admin_settings, name='admin-settings'),
    
]
