from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

def get_rectangle_area(request, wigth: int, height: int):
    return HttpResponse(f'The area of the rectangle {wigth} x {height} equals {int(wigth * height)}')


def get_square_area(request, width: int):
    return HttpResponse(f'The area of the square {width} x {width} equals {int(width * width)}')


def get_circle_area(request, radius: float):
    return HttpResponse(f'Area of a circle with a radius {radius} equals {float(radius * radius * 3.14)}')
