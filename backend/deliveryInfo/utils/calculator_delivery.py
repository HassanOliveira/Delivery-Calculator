from datetime import datetime
from .convert_string_to_time import *
import json

def surchargeCartValue (cartValue):
    # Checks if the value of the cart is less than 10 and returns the fee to be added on delivery.

    if cartValue < 10:
        valueSurchargeCartValue = 10 - cartValue
    else:
        valueSurchargeCartValue = 0
    return valueSurchargeCartValue

def surchargeNumberItems (number_of_items):
    # Checks the number of items and returns the fee to be added on delivery.

    if 5 <= number_of_items <= 12:
        valueSurchargeNumberItems = ((number_of_items - 4) * 0.5)
    elif number_of_items > 12:
        valueSurchargeNumberItems = (((number_of_items - 4) * 0.5) + 1.2)
    else:
        valueSurchargeNumberItems = 0    
    return valueSurchargeNumberItems

def deliveryDistance (distance):
    # Checks the number of items and returns the delivery value without the fees.

    baseFee = 2     # For 1000m.
    minimumFee = 1     # Less than or equal to 500m.
    distanceSurcharge = 1    # Value to be added every 500m.

    if distance <= 500:
        valueDeliveryPrice = minimumFee
    elif 501 <= distance <= 1000:
        valueDeliveryPrice = baseFee
    elif distance >= 1001:
        valueDeliveryPrice = (baseFee + (distanceSurcharge * (round(((distance/500) - 2) + 0.5))))
    return valueDeliveryPrice

def deliveryPrice (valueSurchargeCartValue, valueSurchargeNumberItems, valueDeliveryPrice, cartValue, time):
    # Receives all calculated values and returns the final value of the delivery according to the established rules.

    totalPrice = (valueSurchargeCartValue + valueSurchargeNumberItems + valueDeliveryPrice)  # Sum of fees and delivery value.
    rush = 1.2   # Rush hour multiplier.
    time15 = time15h()  # Function to convert string to datetime.
    time19 = time19h()  # Function to convert string to datetime.
    time = actualTime(time)  # Function to convert input string to datetime.

    if  datetime.utcnow().weekday() == 4 and time15 <= time <= time19:  # In case you are not on a Friday, here you need to switch to "or" to see the addition in the calculation, as this function checks the day and time of the request.
        totalPrice = totalPrice*rush      
    if totalPrice > 15 and cartValue < 100:
        deliveryPrice = {'totalPrice': 15}
    elif cartValue >= 100:
        deliveryPrice = {'totalPrice': 0}
    else:
        deliveryPrice = {'totalPrice': totalPrice}
    print(f'5{deliveryPrice}')

    return json.dumps(deliveryPrice['totalPrice'])