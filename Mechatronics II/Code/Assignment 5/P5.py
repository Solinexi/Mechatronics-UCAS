"""
This program creates a 2D tuple which contains positions, sizes, and colors of a star(s). Then unpacks the tuple into a for loop which sets the colorfill, draws the star, and ends the fill.
"""
import turtle as t # Imports Turtle
t.speed(0) # Sets Turtle speed to max

# This defines our nested 2D tuple of stars
draw = ((130, 104, 50, "blue"),
        (200, 164, 60, "red"),
        (330, 140, 20, "green"),
        (30, 144, 40, "yellow"),
        (-90, 94, 100, "black",))

for x, y, size, color in draw: # Unpacks our tuple into 4 varibles, for use in a for loop
    t.teleport(x, y) # Moves our turtle to the tuple X and Y
    t.fillcolor(color) # Sets our fill color using tuple Color
    t.begin_fill() # Begins filling the star
    for _ in range(5): # Loops 5 times
        t.fd(size/2) # Moves the turtle forward our size divided by 2
        t.lt(72) # Turns turtle right by 72 Degrees
        t.fd(size/2) # Moves the turtle forward our size divided by 2
        t.rt(144) # Turns turtle right by 144 Degrees
    t.end_fill() # Ends our fill
        
t.done() # Finishes Program
