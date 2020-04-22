from rest_framework import serializers
from .models import Product, Rating
from django.db.models import Count
from django.db.models import Avg

class ProductSerializer(serializers.ModelSerializer):
    rating_count = serializers.SerializerMethodField()
    rating_average = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ["name", "description", "image", "price", "rating_count", "rating_average"]
    
    def get_rating_count(self, obj):
         return Rating.objects.filter(product__id=obj.id).count()

    def get_rating_average(self, obj):
        return Rating.objects.filter(product__id=obj.id).aggregate(Avg('rating'))["rating__avg"]


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ['product', 'rating']


    