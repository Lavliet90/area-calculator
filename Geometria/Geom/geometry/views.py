from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string
from django.shortcuts import render


def get_rectangle_area(request, width: int, height: int):
    data = {
        'the_size_x': int(width),
        'the_size_y': int(height),
        'equals': int(width * height),
    }
    return render(request, 'geometry/rectangle.html', context=data)


def get_square_area(request, width: int):
    data = {
        'the_size': int(width),
        'equals': int(width ** 2),
    }
    return render(request, 'geometry/square.html', context=data)


def get_circle_area(request, radius: int):
    data = {
        'radius': int(radius),
        'equals': float(radius ** 2 * 3.141),
    }
    return render(request, 'geometry/circle.html', context=data)
