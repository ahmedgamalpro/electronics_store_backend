from rest_framework.serializers import ModelSerializer
from .models import Cart,CartItem


class CartSerializer(ModelSerializer):

    class Meta:
        model = Cart
        fields = ('id', 'created_by', 'status','created_at','updated_at')


class CartItemSerializer(ModelSerializer):

    class Meta:
        model = CartItem
        fields = ('cart_id ', 'product_id', 'price','quantity')