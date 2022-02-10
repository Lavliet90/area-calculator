# area-calculator

Recently, I have been a little busy, so I decided to have fun with simple tasks. Specifically, here is the task on the url.

In the application's urls.py file, three routes need to be processed:

path(rectangle/<int:width>/<int:height>, views.get_rectangle_area)
path(square/<int:width>, views.get_square_area)
path(circle/<int:radius>, views.get_circle_area)

Each route must find the area of the corresponding figure.

For example, accessing the path http://127.0.0.1:8000/geometry/rectangle/10/5 we should get the following response:

The area of a 10x5 rectangle is 50
