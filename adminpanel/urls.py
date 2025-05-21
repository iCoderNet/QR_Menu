from django.urls import path
from .views import *

urlpatterns = [
    path('', admin_dashboard, name='admin-dashboard'),
    path('login/', admin_login, name='admin-login'),
    path('logout/', admin_logout, name='admin-logout'),
    
]
