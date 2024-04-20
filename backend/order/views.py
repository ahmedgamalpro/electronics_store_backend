from django.shortcuts import render
from rest_framework import status
from rest_framework import permissions
from .models import Order,OrderLine
from rest_framework import viewsets
from rest_framework.response import Response
from .serializer import OrderSerializer,OrderLineSerializer
from django.shortcuts import get_object_or_404
from rest_framework.decorators import action
# Create your views here.

#List view

class OrderLineViewSet(viewsets.ViewSet):
    queryset = OrderLine.objects.all()
    
    permission_classes = [permissions.AllowAny]
    
    def list(self,request):
        serializer = OrderLineSerializer(self.queryset,many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        orderLine = get_object_or_404(self.queryset, pk=pk)
        serializer = OrderLineSerializer(orderLine)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(serializer)

        return Response(serializer.data, status=status.HTTP_201_CREATED)
    def destroy(self, request):
        orderLine = self.get_object()
        orderLine.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    @action(detail=False, methods=['get'])
    def OrderLines_not_done(self, request):
        OrderLine_count = OrderLine.objects.filter(done=False).count()

        return Response(OrderLine_count)

OrderLine_list = OrderLineViewSet.as_view({'get': 'list'})
OrderLine_detail = OrderLineViewSet.as_view({'get': 'retrieve'})


class OrderViewSet(viewsets.ViewSet):
    queryset = Order.objects.all()
    
    permission_classes = [permissions.AllowAny]
    
    def list(self,request):
        serializer = OrderSerializer(self.queryset,many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        order = get_object_or_404(self.queryset, pk=pk)
        serializer = OrderSerializer(order)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(serializer)

        return Response(serializer.data, status=status.HTTP_201_CREATED)
    def destroy(self, request):
        order = self.get_object()
        order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    @action(detail=False, methods=['get'])
    def Orders_not_done(self, request):
        Order_count = Order.objects.filter(done=False).count()

        return Response(Order_count)

Order_list = OrderViewSet.as_view({'get': 'list'})
Order_detail = OrderViewSet.as_view({'get': 'retrieve'})
