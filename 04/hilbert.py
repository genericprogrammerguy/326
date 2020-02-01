from turtle import *

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

def hilbert_curve(turtle: object, x: object, y: object, xi, xj, yi, yj, n: object) -> object:

    # recursive call
    if n <= 0:
        return
        x = (x + (xi + yi)/2)
        y = (y + (xj + yj)/2)
    # print('%s %s 0' % (X,Y))
    else:
        #turtle.left(y * 90)
        # Point A
        turtle.left.hilbert_curve(x, y, yi/2, yj/2, xi/2, xj/2, n - 1)

        turtle.foward(x)

        #turtle.right(y * 90)
        # Point B
        turtle.right.hilbert_curve(x + xi/2, y + xj/2, xi/2, xj/2, yi/2, yj/2, n - 1)

        turtle.foward(x)

        # turtle.right(y * 90)
        # Point C
        turlte.right.hilbert_curve(x + xi/2 + yi/2, y + xj/2 + yj/2, xi/2, xj/2, yi/2, yj/2, n - 1)

        turtle.foward(x)
        # Point D
        hilbert_curve(x + xi/2 + yi, y + xj/2 + yj, -yi/2,-yj/2,-xi/2, -xj/2, n - 1)
        #turlte.left(x * 90)

if __name__ == "___main___":

    s = Screen()

    t = Turtle()
    t.shape('turtle')
    t.speed('slow')
    n = 3

    hilbert_curve(x, y ,xi, xj, yi, yj, n)

