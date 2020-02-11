from turtle import Screen, Turtle


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

order = 6

def hilbert(t,dir, rot, order):
    if( order == 0):
        return

    # POINT A
    #dir = dir - rot
    t.right(rot * 90)
    print("(R)")
    hilbert(t, dir, - rot, order - 1)
    t.forward(dir)
    print("F")
    
    # POINT B
    #dir = dir - rot
    t.left(rot * 90)
    print("((L))")
    hilbert(t, dir,  rot, order - 1)
    t.forward(dir)
    print("F")

    #POINT C
    #dir = dir - rot
    print("(((L)))")
    hilbert(t, dir,  rot, order - 1)
    t.left(rot * 90)
    t.forward(dir)
    print("F")

    # POINT D
    #dir = dir - rot
    hilbert(t, dir, - rot, order - 1)
    t.right(rot * 90)
    print("((((R))))")

def rescale():
    t.reset()
    t.speed("fastest")
    s.setworlscoordinates(0,0,2**order-1,2**order-1)
    hilbert(t, length, rot, order)
    s.update()
    s.ontimer(rescale, 1000)

def main():
    length = 100/(4*order-1)
    s = Screen()
    s.tracer(False)
    t = Turtle()

    hilbert(t, 10, 1, order)

    s.mainloop()

if __name__ =="__main__":
    main()