import turtle
import sys

def hilbert(t,dir, rot, order):
    """
    Is a method to recursively call the drawing of the Hilbert Curve

    :param t: turtle
    :param dir: direction
    :param rot:  rotation
    :param order: magnitude
    :return: None
    """
    if( order == -1):
            return

    # POINT A
    #dir = dir - rot
    t.right(rot * 90)
    #print("(R)")
    hilbert(t, dir, - rot, order - 1)
    t.forward(dir)
    #print("F")
    
    # POINT B
    #dir = dir - rot
    t.left(rot * 90)
    #print("((L))")
    hilbert(t, dir,  rot, order - 1)
    t.forward(dir)
    #print("F")

    #POINT C
    #dir = dir - rot
    #print("(((L)))")
    hilbert(t, dir,  rot, order - 1)
    t.left(rot * 90)
    t.forward(dir)
    #print("F")

    # POINT D
    #dir = dir - rot
    hilbert(t, dir, - rot, order - 1)
    t.right(rot * 90)
    #print("((((R))))")

def rescale(x,y):
    """
    A method to rescale the screen and hilbert curve

    :return: None
    """
    t.reset() #resets x & y
    t.clear() #clears screen of any drawing
    s = t.getscreen() # gets screen
    #t.speed("fastest")
    s.setworldcoordinates(0,0,(2**order-1),-(2**order-1))
    t.goto(0,0)
    hilbert(t, 1, 1, order)
    #hilbert(t, 1, 1, order)


def main():
    """
    Main method
    Main driver of program. Prompts user for input of the order of magnitude for hilbert curve
    The sets the turtle environment up and then recursively draws the hilbert curve while also
    rescaling the screen

    :return: None
    """
    print("Enter Magnitude of Hilbert Curve:")
    global order
    order = int(input())
    global t
    t = turtle.Turtle()
    #t.hideturtle()
    s = t.getscreen()
    s.tracer(False)
    #print(turtle.turtles())
    t.left(90)
    hilbert(t, 1, 1, order)
    rescale(0,0)
    s.listen()
    #s.ontimer(rescale, 100)
    s.onclick(rescale)
    s.mainloop()

if __name__ =="__main__":
    main()