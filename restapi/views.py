from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from main.models import Restaurant, Menu, Category, MenuItem
from .serializers import RestaurantSerializer, CategorySerializer, MenuItemSerializer

class PublicCategoryList(APIView):
    def get(self, request, restaurant_id):
        try:
            restaurant = Restaurant.objects.get(pk=restaurant_id)
        except Restaurant.DoesNotExist:
            return Response({"detail": "Restaurant not found."}, status=status.HTTP_404_NOT_FOUND)

        active_menu = Menu.objects.filter(restaurant=restaurant, is_active=True).first()
        if not active_menu:
            return Response({"detail": "No active menu found for this restaurant."}, status=status.HTTP_404_NOT_FOUND)

        categories = Category.objects.filter(menu=active_menu)
        data = {
            "restaurant": RestaurantSerializer(restaurant).data,
            "categories": CategorySerializer(categories, many=True).data
        }
        return Response(data)


class PublicProductList(APIView):
    def get(self, request, restaurant_id):
        try:
            restaurant = Restaurant.objects.get(pk=restaurant_id)
        except Restaurant.DoesNotExist:
            return Response({"detail": "Restaurant not found."}, status=status.HTTP_404_NOT_FOUND)

        active_menu = Menu.objects.filter(restaurant=restaurant, is_active=True).first()
        if not active_menu:
            return Response({"detail": "No active menu found for this restaurant."}, status=status.HTTP_404_NOT_FOUND)

        categories = Category.objects.filter(menu=active_menu)
        items = MenuItem.objects.filter(category__in=categories, available=True)

        data = {
            "restaurant": RestaurantSerializer(restaurant).data,
            "products": MenuItemSerializer(items, many=True).data
        }
        return Response(data)
