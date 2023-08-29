
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from rest_tms.views import Products, ProductInfo

urlpatterns = [
    path('', Products.as_view()),
    path('<int:pk>/', ProductInfo.as_view()),

]

# Если используем метакотроллеры
# router = DefaultRouter()
# router.register('havka', Products, basename='prod')
# urlpatterns = [
#     path('', include(router.urls)),
#
# ]


