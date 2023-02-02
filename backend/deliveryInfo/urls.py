from django.urls import path
from . import views


urlpatterns = [
    path('deliveryinfo/calculate', views.calculatorView.as_view()),
]