from rest_framework import serializers
from main.models import Restaurant, Category, MenuItem

class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ['id', 'name', 'address', 'phone']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'sort_order']

class MenuItemSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()  # yoki `category.name`

    class Meta:
        model = MenuItem
        fields = ['id', 'name', 'description', 'price', 'image_url', 'available', 'category']
