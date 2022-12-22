from rest_framework import serializers
from app.feedback.models import (
    Comment
)

class CommentSerializer(serializers.ModelSerializer):
    owner = serializers.EmailField(required=True)
    
    class Meta:
        model = Comment
        fields = '__all__'