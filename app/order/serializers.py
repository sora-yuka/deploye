from rest_framework import serializers
from app.order.tasks import send_confirmation_email
from app.order.models import Order

class OrderSerializer(serializers.ModelSerializer):
    owner = serializers.EmailField(required=False)
    
    class Meta:
        model = Order
        fields = '__all__'
        
    def create(self, validated_data):
        amount = validated_data['amount']
        product = validated_data['product']
        
        if amount > product.amount:
            raise serializers.ValidationError('We dont have so mush paskages')
        if amount == 0:
            raise serializers.ValidationError('You entered 0, son of a bitch')
        
        product.amount -= amount
        product.save(update_fields=['amount'])
        order = Order.objects.create(**validated_data)
        send_confirmation_email.delay(order.owner.email, 
                                order.activation_code, 
                                order.product.name, 
                                order.total_price)
        return super().create(validated_data)