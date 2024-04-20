
from django.urls import path, include
from .views import (
    OrderViewSet,
    OrderViewSet
)

from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns

router = routers.SimpleRouter()
router.register(r'order', OrderViewSet,basename='order')
router.register(r'orderline', OrderViewSet,basename='orderline')

urlpatterns = [
    
    path('', include(router.urls)),
]

urlpatterns += router.urls

urlpatterns = format_suffix_patterns(urlpatterns)

