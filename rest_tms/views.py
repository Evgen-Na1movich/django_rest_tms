from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.routers import DefaultRouter
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from rest_tms.models import Product
from rest_tms.serializer import ProductSerializer

# @api_view(['GET', 'POST'])
# def products(request):
#     if request.method == 'GET':
#         products = Product.objects.all()
#         serializer = ProductSerializer(products, many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = ProductSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=201)
#         return Response(serializer.errors, status=400)
#
#
# @api_view(['GET', 'PUT', 'DELETE'])
# def get_product_detail(request, pk):
#     product = Product.objects.get(pk=pk)
#     if request.method == 'GET':
#         serializer = ProductSerializer(product)
#         return Response(serializer.data)
#     elif request.method == 'PUT':
#         serializer = ProductSerializer(product, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=200)
#         return Response(serializer.errors, status=400)
#     elif request.method == 'DELETE':
#         product.delete()
#         return Response(status=204)


"""
Использование классов для описания api.
Как описать api через классы?
Нужно описать 2 класса, наследуясь от APIView(контроллер класса) 
из rest_framework.views. Первый класс содержит методы get и post, 
второй класс содержит методы get, put и delete. 
Для регистрации классов нужно в path передать имя класса, 
вызвав метод класс .as_view()

"""
# class Products(APIView):
#     def get(self, request):
#         products = Product.objects.all()
#         serializer = ProductSerializer(products, many=True)
#         return Response(serializer.data)
#
#     def post(self, request):
#         serializer = ProductSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=201)
#         return Response(serializer.errors, status=400)
#
#
# class ProductInfo(APIView):
#     def get(self, request, pk):
#         product = Product.objects.get(pk=pk)
#         serializer = ProductSerializer(product)
#         return Response(serializer.data)
#
#     def put(self, request, pk):
#         product = Product.objects.get(pk=pk)
#         serializer = ProductSerializer(product, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=201)
#         return Response(serializer.errors, status=400)
#
#     def delete(self, request, pk):
#         product = Product.objects.get(pk=pk)
#         product.delete()
#         return Response(status=204)

"""
Использование контроллеры-классов высокого уровня для описания API
Как описать api через контроллеры классы высокого уровня?
Нужно описать 2 класса, наследуясь от ListCreateAPIView и RetrieveUpdateDestroyAPIView 
из rest_framework.generics. 
Внутри классов нужно определить атрибуты класса queryset и serializer_class
"""


class Products(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    # фильтрация по visible=True
    # def get_queryset(self):
    #     # получаем queryset, который есть и переопределяем его
    #     queryset = super(Products, self).get_queryset()
    #     queryset = queryset.filter(visible=True)
    #     return queryset


class ProductInfo(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


"""
Использование метакотроллеров
Как описать api через метаконтроллеры?
Нужно описать 1 класса, наследуясь от ModelViewSet из rest_framework.viewsets. 
Для регистрации необходимо в urls.py создать объект DefaultRouter 
и вызвать метод register, передав строку доступа в урле и класс. 
Затем включить все урлы с помощью include() 
"""


# class Products(ModelViewSet):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
