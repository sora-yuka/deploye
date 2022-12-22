from rest_framework import status
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Order
from rest_framework.generics import get_object_or_404
from .serializers import OrderSerializer

class OrderAPIView(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
        
    def get_queryset(self):
        return super().get_queryset()
        queryset = queryset.filter(owner=self.request.user)
        return queryset
    
    
class OrderConfirmationAPIView(APIView):
    def get(self, request, code):
        order = get_object_or_404(Order, activation_code=code)    
        if not order.is_confirm:
            order.is_confirm = True
            order.status = 'in_processing'
            order.save(update_fields=['is_confirm', 'status'])
            return Response({'message': 'You have confirmed order'}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'You already have confirmed your order'}, status=status.HTTP_400_BAD_REQUEST)