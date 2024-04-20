
from django.urls import path, include
from .views import (
    ProductViewSet,
    CategoryViewSet
)

from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns

router = routers.SimpleRouter()
router.register(r'product', ProductViewSet,basename='product')
router.register(r'category', CategoryViewSet,basename='category')

urlpatterns = [
    
    path('', include(router.urls)),
]

urlpatterns += router.urls

urlpatterns = format_suffix_patterns(urlpatterns)

