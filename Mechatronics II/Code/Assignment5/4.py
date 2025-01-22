"""
This program creates 3 lists then zips them to be used as a tuple in a for loop, it uses these values to move around a turtle
"""
import turtle as t # Imports Turtle
t.speed(0) # Sets Turtle speed to max

x=(100, 100, 100, 100,) # Creates our X value list
turn=(90, 90, 90, 90,) # Creates our Turn value list
y=(125, 135, 145, 155,) # Creates our Y value list

for x, turn, y in zip(x,turn,y): # pulls out 3 values from the zipped list
    t.fd(x) # Moves turtle forward by X
    t.rt(turn) # Turns turtle right by Turn
    t.fd(y) # Turns turtle right by Y

t.done() # Finishes Program
