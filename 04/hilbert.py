import sys, math

def hilbert_curve(x, y, xi, xj, yi, yj, n):
    # recursive call
    if n <= 0:
        X = (x + (xi + yi)/2)
        Y = (y + (xj + yj)/2)

        print('%s %s 0' % (X,Y))
    else:
        hilbert_curve(x,                    y,                   yi/2, yj/2, xi/2, xj/2, n - 1)
        hilbert_curve(x + xi/2,             y + xj/2,            xi/2, xj/2, yi/2, yj/2, n - 1)
        hilbert_curve(x + xi/2 + yi/2,      y + xj/2 + yj/2,     xi/2, xj/2, yi/2, yj/2, n - 1) 
        hilbert_curve(x + xi/2 + yi,        y + xj/2 + yj,       -yi/2,-yj/2,-xi/2, -xj/2, n - 1)
        

def main():
    arg = sys.argv
    pixels = float(arg[1])
    ctype = arg[2]
    reps = int(arg[3])
    width = float(arg[4])

    curves = int(math.pow(4, reps))

    hilbert_curve(0.0, 0.0, 1.0, 0.0, 1.0, 0.0, reps)

#    print('] \"constanatwidth\" [%s]' % width)

if __name__ == "__main__":
    main()
