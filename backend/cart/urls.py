
from django.urls import path, include
from .views import (
    CartItemViewSet,
    CartViewSet
)

from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns

router = routers.SimpleRouter()
router.register(r'cart', CartViewSet,basename='cart')
router.register(r'cartitem', CartItemViewSet,basename='cartitem')

urlpatterns = [
    
    path('', include(router.urls)),
]

urlpatterns += router.urls

urlpatterns = format_suffix_patterns(urlpatterns)

