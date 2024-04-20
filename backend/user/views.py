from django.shortcuts import render
from rest_framework import status
from rest_framework import permissions
from .models import User
from rest_framework import viewsets
from rest_framework.response import Response
from .serializer import UserSerializer
from django.shortcuts import get_object_or_404
from rest_framework.decorators import action
# Create your views here.

#List view

class UserViewSet(viewsets.ViewSet):
    queryset = User.objects.all()
    
    permission_classes = [permissions.AllowAny]
    
    def list(self,request):
        serializer = UserSerializer(self.queryset,many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        user = get_object_or_404(self.queryset, pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(serializer)

        return Response(serializer.data, status=status.HTTP_201_CREATED)
    def destroy(self, request):
        user = self.get_object()
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    @action(detail=False, methods=['get'])
    def Users_not_done(self, request):
        user_count = User.objects.filter(done=False).count()

        return Response(user_count)

User_list = UserViewSet.as_view({'get': 'list'})
User_detail = UserViewSet.as_view({'get': 'retrieve'})



