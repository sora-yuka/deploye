from django.db import models
from django.contrib.auth import get_user_model
from app.product.models import Product
import uuid

User = get_user_model()

class Order(models.Model):
    ORDER_STATUS = (
        ('in_processing', 'in_processing'),
        ('completed', 'completed'),
        ('declined', 'declined')
    )
    
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='orders')
    status = models.CharField(max_length=30, choices=ORDER_STATUS, null=True, blank=True)
    is_confirm = models.BooleanField(default=False)
    amount = models.PositiveIntegerField()
    address = models.CharField(max_length=80)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    activation_code = models.UUIDField(default=uuid.uuid4)
        
    def save(self, *args, **kwargs):
        self.total_price = self.amount * self.product.price
        return super().save(*args, **kwargs)