# importing datetime module
from datetime import datetime

def time15h ():
    time_str = '15:00'
    time_object = datetime.strptime(time_str, '%H:%M').time()
    return time_object

def time19h ():
    time_str = '19:00'
    time_object = datetime.strptime(time_str, '%H:%M').time()
    return time_object

def actualTime (time):
    time_str = time
    time_object = datetime.strptime(time_str, '%H:%M').time()
    return time_object