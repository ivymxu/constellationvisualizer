# Purpose: Writing a program with conditionals and decisions that draws stars.

from SimpleGraphics import *

background("black")

print("This program draws constellations based on user-driven input")

# CONSTANTS
SCREENX = 800
SCREENY = 600
HORIZONTALBUFFER = 100
TICKDISTANCE = 75
XAXIS = 100
XLABEL = -1.0
LABELDISTANCE = 0.25
YAXIS = 0
YLABEL = 1.0
EDGECOLOR = "red"

resize(SCREENX, SCREENY)

# DRAW AXES
setOutline("blue")
line(HORIZONTALBUFFER, SCREENY/2, SCREENX-HORIZONTALBUFFER, SCREENY/2)
line(SCREENX/2, SCREENY-600, SCREENX/2, SCREENY)

# Draw tick marks and labels for the x-axis
while XAXIS <= SCREENX-100:
    text(XAXIS, SCREENY/2, "|")
    # text(XAXIS,SCREENY/2+15, -1+(0.25*(XAXIS=100)/75))
    if XLABEL != 0:
        text(XAXIS, SCREENY/2+15, XLABEL)  # 10px so that text is visible
    else:
        text(XAXIS+10, SCREENY/2+15, int(XLABEL))
    XAXIS += TICKDISTANCE
    XLABEL += LABELDISTANCE

# Draw tick marks and labels for the y-axis
while YAXIS <= SCREENY:
    text(SCREENX/2, YAXIS, "--")
    if YLABEL != 0:
        text(SCREENX/2+17, YAXIS, YLABEL)
    YAXIS += TICKDISTANCE
    YLABEL += -LABELDISTANCE

# DRAW CONSTELLATIONS

# Ask user the number of stars
starcount = int(input("Input count of constellation stars (<=0 to exit): "))

while starcount > 0:
    for i in range(starcount):
        # Ask user to x and y coordinates and magnitude of stars
        inputX = float(input("Give star x coordinate (between -1.0 and 1.0): "))
        inputY = float(input("Give star y coordinate (between -1.0 and 1.0): "))
        magnitude = float(input("Give star magnitude (-2 < magnitude <= 10.5): "))
        size = 10/(magnitude+2)
        xTick = 400+(inputX/0.25)*75-size/2
        yTick = 300-(inputY/0.25)*75-size/2
        setColor("white")
        setOutline("white")
        ellipse(xTick, yTick, size, size)
    if starcount > 0:
        # Ask user the number of constellation edges
        edgecount = int(input("Input how many constellation edges to plot: "))
        for j in range(edgecount):
            # Ask user the x and y coordinates of the constellation edges
            inputX1 = float(input("Give star1 x coordinate (between -1.0 and 1.0): "))
            inputY1 = float(input("Give star1 y coordinate (between -1.0 and 1.0): "))
            inputX2 = float(input("Give star2 x coordinate (between -1.0 and 1.0): "))
            inputY2 = float(input("Give star2 y coordinate (between -1.0 and 1.0): "))
            xline = 400+(inputX1/0.25)*75
            yline = 300-(inputY1/0.25)*75
            xline1 = 400+(inputX2/0.25)*75
            yline1 = 300-(inputY2/0.25)*75
            setOutline(EDGECOLOR)
            line(xline, yline, xline1, yline1)
            # I attempted to create a box for each constellation, but I could only reach to this point because I kept getting a TypeError
            minx1 = int(min(str(inputX))-15)
            miny1 = int(min(str(inputY))-15)
            maxx2 = int(max(str(inputX))+15)
            maxy2 = int(max(str(inputY))+15)
            setOutline("orange")
            line(minx1, miny1, minx1, maxy2, minx1, maxy2, maxx2, maxy2, maxx2, maxy2, maxx2, miny1, maxx2, miny1, minx1, miny1)
        else:
            starcount = int(input("Input count of constellation stars (<=0 to exit): "))
    # Looping red, green, and yellow for the constellation edges
    if EDGECOLOR == "red":
        EDGECOLOR = "green"
    elif EDGECOLOR == "green":
        EDGECOLOR = "yellow"
    else:
        EDGECOLOR = "red"
        setOutline(EDGECOLOR)
print("End of program")
