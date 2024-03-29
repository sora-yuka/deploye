from rest_framework import serializers
from app.product.models import (
    Category, Product, Image
)


class ImageSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Image
        fields = '__all__'


class CategorySerializers(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = '__all__'
        
    
    def validate_title(self, title):
        if Category.objects.filter(title=title.lower()).exists():
            raise serializers.ValidationError('such category already exist')
        return title
    

class ProductSerializers(serializers.ModelSerializer):
    owner = serializers.EmailField(required=False)
    file_image = ImageSerializer(many=True, read_only=True)
    
    class Meta:
        model = Product
        fields = '__all__'
        
    def create(self, validated_data):
        request = self.context.get('request')
        product = Product.objects.create(**validated_data)
        files = request.FILES
        list_images = []
        
        for image in files.getlist('images'):
            list_images.append(Image(product=product, image=image))
        Image.objects.bulk_create(list_images)
        return product
