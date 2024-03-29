from django.contrib import admin
from app.order.models import Order

class OrderAdmin(admin.ModelAdmin):
    list_display = ['owner', 'product', 'status', 'total_price', 'amount']


admin.site.register(Order, OrderAdmin)