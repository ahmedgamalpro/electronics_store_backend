from rest_framework.serializers import ModelSerializer 
from .models import Order,OrderLine

class OrderSerializer(ModelSerializer):

    class Meta:
        model = Order
        fields = "__all__"



class OrderLineSerializer(ModelSerializer):

    class Meta:
        model = OrderLine
        fields = "__all__"