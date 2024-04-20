from django.contrib import admin
from .models import Order, OrderLine
# Register your models here.
class OrderAdmin(admin.ModelAdmin):
    list_display = ["id","user_id","created_at"]

admin.site.register(Order, OrderAdmin)


class OrderLineAdmin(admin.ModelAdmin):
    list_display = ["id", "order_id","price","quantity"]

admin.site.register(OrderLine, OrderLineAdmin)