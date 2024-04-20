
from django.contrib import admin
from django.urls import path,include
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView,
                                            TokenVerifyView)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('product.urls')),
    path('api/v1/', include('user.urls')),
    path('api/v1/', include('order.urls')),
    path('api/v1/', include('cart.urls')),
    path('token/create/', TokenObtainPairView.as_view(), name='token_create'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
