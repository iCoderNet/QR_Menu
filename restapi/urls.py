from django.urls import path
from .views import PublicCategoryList, PublicProductList

urlpatterns = [
    path('public/<int:restaurant_id>/categories/', PublicCategoryList.as_view(), name='public-categories'),
    path('public/<int:restaurant_id>/products/', PublicProductList.as_view(), name='public-products'),
]