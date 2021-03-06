###############################################
# Name: Taylor Kirk
# Class: CMPS 4663 Cryptography
# Date: 1 August 2015
# Program 3 - Elliptical Curve Encryption
###############################################

import numpy as np
import matplotlib.pyplot as plt
import argparse
import sys

def main():
    
    parser = argparse.ArgumentParser()
    parser.add_argument("-a", "--scalar", dest="a", help="Given y^2 = x^3 + a*x + b: Input 'a'")
    parser.add_argument("-b", "--constant", dest="b", help="Given y^2 = x^3 + a*x + b: Input 'b'")
    parser.add_argument("-x1", "--firstXValue", dest="x1", help="Given P1(x1,y1): Input x1")
    parser.add_argument("-y1", "--firstYValue", dest="y1", help="Given P1(x1,y1): Input y1")
    parser.add_argument("-x2", "--secondXValue", dest="x2", help="Given P2(x2,y2): Input x2")
    parser.add_argument("-y2", "--secondYValue", dest="y2", help="Given P1(x2,y2): Input y2")
    args = parser.parse_args()
    
    print("a=", args.a, "b=", args.b, "x1=", args.x1, "y1=", args.y1, "x2=", args.x2, "y2=", args.y2)    
    
    a = int(args.a)
    b = int(args.b)
    x1 = int(args.x1)
    y1 = int(args.y1)
    x2 = int(args.x2)
    y2 = int(args.y2)
     
    print("Using Elliptical Curve Equation: y^2 = x^3 +", a, "* x +", b)    
    
    #Test if both given points can be found on given elliptical
    firstCoOrdTest = (x1**3 + a*x1 + b)**(1/2)
    secondCoOrdTest = (x2**3 + a*x2 + b)**(1/2)
    if firstCoOrdTest != y1 or secondCoOrdTest != y2:
        print("Error: Please check given points. One or both are not found on given elliptical")
    else:
        print("Success!!: Both points are found on given elliptical curve")    
    
    #Get the slope of the line
    #if P1 and P2 share either or both of each point's respective
    #x-values or y-values are the same, use derivative form
    #to calculate slope, else, use traditional point-slope formula
    if x1 == x2 and y1 == y2:
        m = (3 * x1**2 + a) / (2 * y1)
        print("Message: Derivative Slope used instead of Point-Slope")
    else:
        m = (y1-y2)/(x1-x2)
    
    #Calculate third point (P3) using slope and P1
    x3 = m**2 - x1 - x2
    y3 = y1 + m * (x3-x1)
    
    #Test to see if P3 is located on Curve
    thirdCoOrdTest = (x3**3 + a*x3 + b)**(1/2)
    if thirdCoOrdTest != y3:
        print("Error: The Point (" , x3 , ',' , y3 , ") was not found on Curve")
    else:
        print("Success!!: 3rd, related Point found at (" , x3 , ',' , y3 , ")")
        
    #Determines width and height of plot
    w = 10  #Default w Value
    h = 12  #Default h Value
    
    xMax = x1
    if xMax < x2:
        xMax = x2
    if xMax < x3:
        xMax = x3
    
    yMax = y1
    if yMax < y2:
        yMax = y2
    if yMax < y3:
        yMax = y3
        
    w = xMax + 3    #w-Value that will be used
    h = yMax + 3    #h-Value that will be used
    
    # Annotate the plot with your name using width (w) and height (h) as your reference points.
    plt.annotate("Taylor Kirk", xy=(-w+2 , h-2),
                 xycoords="data", va="center", ha="center",
                 bbox=dict(boxstyle="round", fc="w"))
    
    # This creates a mesh grid with values determined by width and height (w,h)
    # of the plot with increments of .0001 (1000j = .0001 or 5j = .05)
    y, x = np.ogrid[-h:h:1000j, -w:w:1000j]
    
    # Plot the curve (using matplotlib's countour function)
    # This drawing function applies a "function" described in the
    # 3rd parameter:  pow(y, 2) - ( pow(x, 3) - x + 1 ) to all the
    # values in x and y.
    # The .ravel method turns the x and y grids into single dimensional arrays
    plt.contour(x.ravel(), y.ravel(), pow(y, 2) - ( pow(x, 3) + a*x + b ), [0])
        
    # Plot the points ('ro' = red, 'bo' = blue, 'yo'=yellow and so on)
    plt.plot(x1, y1,'ro')
    
    # Annotate point 1
    plt.annotate('x1,y1', xy=(x1, y1), xytext=(x1+1,y1+1),
        arrowprops=dict(arrowstyle="->",
        connectionstyle="arc3"),
        )    
    
    plt.plot(x2, y2,'ro')
    
    # Annotate point 2
    plt.annotate('x2,y2', xy=(x2, y2), xytext=(x2+1,y2+1),
        arrowprops=dict(arrowstyle="->",
        connectionstyle="arc3"),
        )
    
    # Use a contour plot to draw the line (in pink) connecting our point.
    plt.contour(x.ravel(), y.ravel(), (y-y1)-m*(x-x1), [0],colors=('pink'))
    
    #Plot P3
    plt.plot(x3, y3,'yo')
    
    # Annotate point 3
    plt.annotate('x3,y3', xy=(x3, y3), xytext=(x3+1,y3+1),
        arrowprops=dict(arrowstyle="->",
        connectionstyle="arc3"),
        )
    
    # Show a grid background on our plot
    plt.grid()
    
    # Show the plot
    plt.show()
    
if __name__ == '__main__':
    main()