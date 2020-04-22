from rest_framework import viewsets
from . import serializers
from . import models
from rest_framework.response import Response

class ProductViewSet(viewsets.ModelViewSet):
    http_method_names = ['get']
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer

class RatingViewSet(viewsets.ModelViewSet):
    queryset = models.Rating.objects.all()
    serializer_class = serializers.RatingSerializer