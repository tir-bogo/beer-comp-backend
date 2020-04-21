from django.test import TestCase
from .models import Product, Rating
from rest_framework.test import APIClient
from rest_framework import status
from django.db.models import Avg
from django.db.models import Count


class ProductModelTestCase(TestCase):

    def setUp(self):
        self.product_name = "beer"
        self.product_image = "/img/te.jpg"
        self.product_description = "this is a good beer"
        self.product_price = 12.50
        self.product = Product(name=self.product_name, image=self.product_image, price=self.product_price, description=self.product_description)

    def test_model_can_create_a_product(self):
        old_count = Product.objects.count()
        self.product.save()
        new_count = Product.objects.count()
        self.assertNotEqual(old_count, new_count)

class RatingModelTestCase(TestCase):
    
    def setUp(self):
        self.product_name = "beer"
        self.product_image = "/img/te.jpg"
        self.product_description = "this is a good beer"
        self.product_price = 12.50
        self.product = Product(name=self.product_name, image=self.product_image, price=self.product_price, description=self.product_description)
        self.product.save()

    def test_model_can_create_rating(self):
        old_count = Rating.objects.count()
        rating = Rating(product=self.product, rating=3)
        rating.save()
        new_count = Rating.objects.count()
        self.assertNotEqual(old_count, new_count)
