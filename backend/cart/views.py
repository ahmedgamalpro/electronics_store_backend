from django.shortcuts import render
from rest_framework import status
from rest_framework import permissions
from .models import Cart,CartItem
from rest_framework import viewsets
from rest_framework.response import Response
from .serializer import CartSerializer,CartItemSerializer
from django.shortcuts import get_object_or_404
from rest_framework.decorators import action
# Create your views here.

#List view

class CartItemViewSet(viewsets.ViewSet):
    queryset = CartItem.objects.all()
    
    permission_classes = [permissions.AllowAny]
    
    def list(self,request):
        serializer = CartItemSerializer(self.queryset,many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        CartItem = get_object_or_404(self.queryset, pk=pk)
        serializer = CartItemSerializer(CartItem)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(serializer)

        return Response(serializer.data, status=status.HTTP_201_CREATED)
    def destroy(self, request):
        CartItem = self.get_object()
        CartItem.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    @action(detail=False, methods=['get'])
    def CartItems_not_done(self, request):
        CartItem_count = CartItem.objects.filter(done=False).count()

        return Response(CartItem_count)

CartItem_list = CartItemViewSet.as_view({'get': 'list'})
CartItem_detail = CartItemViewSet.as_view({'get': 'retrieve'})


class CartViewSet(viewsets.ViewSet):
    queryset = Cart.objects.all()
    
    permission_classes = [permissions.AllowAny]
    
    def list(self,request):
        serializer = CartSerializer(self.queryset,many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        cart = get_object_or_404(self.queryset, pk=pk)
        serializer = CartSerializer(cart)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(serializer)

        return Response(serializer.data, status=status.HTTP_201_CREATED)
    def destroy(self, request):
        cart = self.get_object()
        cart.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    @action(detail=False, methods=['get'])
    def Carts_not_done(self, request):
        Cart_count = Cart.objects.filter(done=False).count()

        return Response(Cart_count)

cart_list = CartViewSet.as_view({'get': 'list'})
cart_detail = CartViewSet.as_view({'get': 'retrieve'})
