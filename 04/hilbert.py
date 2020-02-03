from turtle import Screen, Turtle

# the first 2 parameters x and y coordinates are used in the calculation of a point on the hb curve
# the next 4 parameters  xi, xj ,yi ,yj define the two vectors this helps moves the point proportional to x,y vector
#
#            D----------------C
#                             |
#                             |
#                             |
#                             |
#                             |
#                             |
#            A----------------B
#
#          Order1
# n is the order of magnitude

def hilbert_curve(turtle, x, y, xi, xj, yi, yj, n)
    # recursive call
    if n <= 0:
        return
        x = (x + (xi + yi)/2)
        y = (y + (xj + yj)/2)
    
    else:
        turtle.left(y * 90)
        # Point A
        hilbert_curve(turtle, x, y, yi/2, yj/2, xi/2, xj/2, n - 1)

        turtle.foward(x)

        turtle.right(y * 90)
        # Point B
        hilbert_curve(turtle, x + xi/2, y + xj/2, xi/2, xj/2, yi/2, yj/2, n - 1)

        turtle.foward(x)

        turtle.right(y * 90)
        # Point C
        hilbert_curve(turtle, x + xi/2 + yi/2, y + xj/2 + yj/2, xi/2, xj/2, yi/2, yj/2, n - 1)

        turtle.foward(x)
        # Point D
        hilbert_curvet(turtle, x + xi/2 + yi, y + xj/2 + yj, -yi/2,-yj/2,-xi/2, -xj/2, n - 1)
        turtle.left(x * 90)
    
    screen = Screen()
    t = Turtle()   
    hilbert_curve(t, 0.0, 0.0 ,1.0, 0.0, 0.0, 1.0, 2)
    screen.exitonclick()
