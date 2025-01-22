"""
This program creates a 2D touple then unpacks it in a for loop, it uses these values to move around a turtle
"""
import turtle as t # Imports Turtle
t.speed(0) # Sets Turtle speed to max

# This defines our nested 2D tuple
draw = ((150, 90, 125,),
        (100, -90, -75,),
        (50, 90, 25,),
        (-150, 90, -25,))

for dist1, angle, dist2 in draw: # Unpacks our tuple into 3 varibles, for use in a for loop
    t.fd(dist1) # Moves Turtle forward by tuple value one
    t.rt(angle) # Turns Turtle right by tuple value two
    t.fd(dist2) # Moves Turtle forward by tuple value three

t.done() # Finishes Program
