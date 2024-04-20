from django.shortcuts import render
from rest_framework import status
from rest_framework import permissions
from .models import Product,Category
from rest_framework import viewsets
from rest_framework.response import Response
from .serializer import ProductSerializer,CategorySerializer
from django.shortcuts import get_object_or_404
from rest_framework.decorators import action
# Create your views here.

#List view

class ProductViewSet(viewsets.ViewSet):
    queryset = Product.objects.all()
    
    permission_classes = [permissions.AllowAny]
    
    def list(self,request):
        serializer = ProductSerializer(self.queryset,many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        product = get_object_or_404(self.queryset, pk=pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(serializer)

        return Response(serializer.data, status=status.HTTP_201_CREATED)
    def destroy(self, request):
        item = self.get_object()
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    @action(detail=False, methods=['get'])
    def products_not_done(self, request):
        user_count = Product.objects.filter(done=False).count()

        return Response(user_count)

product_list = ProductViewSet.as_view({'get': 'list'})
product_detail = ProductViewSet.as_view({'get': 'retrieve'})




class CategoryViewSet(viewsets.ViewSet):
    queryset = Category.objects.all()
    
    permission_classes = [permissions.AllowAny]
    
    def list(self,request):
        serializer = CategorySerializer(self.queryset,many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        category = get_object_or_404(self.queryset, pk=pk)
        serializer = CategorySerializer(category)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(serializer)

        return Response(serializer.data, status=status.HTTP_201_CREATED)
    def destroy(self, request):
        item = self.get_object()
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    @action(detail=False, methods=['get'])
    def products_not_done(self, request):
        user_count = Category.objects.filter(done=False).count()

        return Response(user_count)


category_list = CategoryViewSet.as_view({'get': 'list'})
category_detail = CategoryViewSet.as_view({'get': 'retrieve'})