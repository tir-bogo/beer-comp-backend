from django.urls import include, path
from rest_framework import routers
from . import views


router = routers.DefaultRouter()
router.register(r'products', views.ProductViewSet)
router.register(r'rating', views.RatingViewSet)

urlpatterns = [
    path('', include(router.urls)),

]