"""
This program creates a 2D tuple then parses through it using a nested for loop, it uses these numbers to move around a turtle
"""
import turtle as t # Imports Turtle
t.speed(0) # Sets Turtle speed to max

# This defines our nested 2D tuple
draw = ((200, 175, 150,), 
        (125, 100, 75,),
        (50, 25, 5,),
        (150, 100, 225,))

for a in range(4): # Outer for loop
    for b in range(3): # Inner for loop
        t.fd(draw[a][b]) # Moves the Turtle forward by amount in tuple
        t.rt(90) # Turns Turtle 90 Degrees

t.done() # Finishes Program
