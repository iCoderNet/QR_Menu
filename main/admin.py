from django.contrib import admin
from .models import *

admin.site.register([User, Menu, Restaurant, QRCode, Visit, Category, MenuItem])