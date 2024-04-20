
from django.urls import path, include
from .views import (
    UserViewSet,
)

from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns

router = routers.SimpleRouter()
router.register(r'user', UserViewSet,basename='user')

urlpatterns = [
    
    path('', include(router.urls)),
]

urlpatterns += router.urls

urlpatterns = format_suffix_patterns(urlpatterns)

