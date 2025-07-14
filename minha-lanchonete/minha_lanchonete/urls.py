from django.urls import path, include
from rest_framework import routers

from minha_lanchonete import views

router = routers.DefaultRouter()

router.register(r'products/drinks', views.DrinkView)
router.register(r'orders', views.OrderView)
router.register(r'payment_methods', views.PaymentMethodView)
router.register(r'products/pizzas', views.PizzaView)
router.register(r'products', views.ProductView)

urlpatterns = [
    path(r'api/', include(router.urls)),
    path(r'auth/', include("users.urls"))
]
