from django.urls import path
from .views import *

urlpatterns = [
    path('', MainView.as_view(), name='main'),
    path('<str:page>', PageHTMLView.as_view()),
]
