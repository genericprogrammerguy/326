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

# def hilbert_curve(t,x, y, xi, xj, yi, yj, n):
#     # recursive call
#     if n < 1:
#         return
#         x = x + (xi + yi)/2
#         print("X")
#         y = y + (xj + yj)/2
#         print("Y")
#     else:
#         # Point A
#         hilbert_curve(t,    x,      y,      yi/2,   yj/2,   xi/2,   xj/2,   n - 1)
#         t.forward(10)
#         print("pointA")
#         # Point B
#         t.left(x * 90)
#         hilbert_curve(t,    x +     xi/2,   y +     xj/2,   xi/2,   xj/2,   yi/2, yj/2, n - 1)
#         t.forward(10)
#         print("pointB")
#         # Point C
#         t.left(y * 90)
#         hilbert_curve(t,    x +     xi/2 +  yi/2,   y +     xj/2 +  yj/2,   xi/2, xj/2, yi/2, yj/2, n - 1)
#         print("pointC")
#         t.forward(10)
#         # Point D
#         t.left(x * 90)
#         hilbert_curve(t,    x +     xi/2 +  yi,     y +     xj/2 +  yj,     -yi/2,-yj/2,-xi/2, -xj/2, n - 1)
#         print("pointD")



def hilbert(dir, rot, order):



def rescale():
    turtle.reset()
    screen.setworlscoordinates()
    hilbert_curve()
    screen.update()
    screen.ontimer(rescale)
    pass
    

if __name__ =="__main__":
    s = Screen()
    t = Turtle()

    herbert(1,2,3)
    # hilbert_curve(t,0.0, 0.0 ,1.0, 0.0, 0.0, 1.0, 4)

    s.mainloop()
