from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import APIView, Request, Response, status
from .utils.calculator_delivery import *
from .utils.convert_string_to_time import *

# Create your views here.

class calculatorView (APIView):
    def post(self, request):
        return Response(deliveryPrice(surchargeCartValue(request.data['cartValue']), surchargeNumberItems(request.data['number_of_items']), deliveryDistance(request.data['distance']), request.data['cartValue'], request.data['time']), status=201)