from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    # Qo‘shimcha fieldlar kerak bo‘lsa shu yerga qo‘shamiz
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('owner', 'Owner'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='owner')


class Restaurant(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='restaurants')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class QRCode(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='qr_codes')
    qr_url = models.URLField()
    code = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.code


class Menu(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='menus')
    title = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Category(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name='categories')
    name = models.CharField(max_length=100)
    sort_order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['sort_order']

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='items')
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image_url = models.URLField(blank=True, null=True)
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Visit(models.Model):
    qr_code = models.ForeignKey(QRCode, on_delete=models.CASCADE, related_name='visits')
    ip_address = models.GenericIPAddressField()
    user_agent = models.TextField()
    visited_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.qr_code.code} - {self.visited_at}"
