from django import urls
from django.urls import path, include
from rest_framework import routers
from ecomm import views

router = routers.DefaultRouter()

router.register("User", viewset=views.UserView, basename="user")
router.register("Product", viewset=views.ProductView, basename="product")

urlpatterns = [
    path("api/", include(router.urls)),
]
