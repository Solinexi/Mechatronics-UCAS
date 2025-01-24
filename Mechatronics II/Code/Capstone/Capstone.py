"""
This program creates a 2D tuple which is parsed through a list in order to make a drawing, it does this by parsing through a tuple in a for loop and running functions associated with diffrent kinds of shapes. 
"""
import turtle as t # Imports the Turtle Library

t.speed(0) # Sets max Turtle speed

# Creates a 2D tuple to store our drawing
draw = (("c",65,-125,100,"black"), 
        ("s",0,0,100,"red"),
        ("s",33,-10,50,"green"),
        ("s",49,-15,25,"blue"),
        ("r",17.5,-120,100,"orange"),
        ("t",40,75,50,"pink"),
        ("t",40,100,50,"pink"),
        ("t",40,125,50,"pink"))

def init(): # Initilizes our Turtle 
     t.teleport(0, 0) # Moves our Turtle to (0,0)
     t.setheading(0) # Sets Turtle angle to 0 degrees

def circle(x, y, size, color): # Defines function to draw a circle 
    t.teleport(x, y) # Moves Turtle to specified cord's 
    t.fillcolor(color) # Sets the Turtle fill color
    t.begin_fill() # Begins filling
    t.circle(size) # Uses bulit in circle function
    t.end_fill() # Ends Filling

def rectangle(x, y, size, color): # Defines function to draw a rectangle
    t.teleport(x, y) # Moves Turtle to specified cord's
    t.fillcolor(color) # Sets the Turtle fill color
    t.begin_fill() # Sets the Turtle fill color
    for _ in range(4): # Defines a loop that will run 4 times
        t.fd(size) # Moves Turtle forward as specified by size
        t.rt(90) # Turns Turtle right by 90 degrees
    t.end_fill() # Ends Filling 
    
def star(x, y, size, color): # Defines function to draw a star
    t.teleport(x, y) # Moves Turtle to specified cord's
    t.fillcolor(color) # Sets the Turtle fill color
    t.begin_fill() # Sets the Turtle fill color
    for _ in range(5): # Defines a loop that will run 5 times
        t.fd(size/2) # Moves Turtle forward as specified by size / 2
        t.lt(72) # Turns Turtle left by 72 degrees
        t.fd(size/2) # Moves Turtle forward as specified by size / 2
        t.rt(144) # Turns Turtle right by 144 degrees
    t.end_fill() # Ends Filling 
    
def triangle(x, y, size, color): # Defines function to draw a triangle
    t.teleport(x, y) # Moves Turtle to specified cord's 
    t.fillcolor(color) # Sets the Turtle fill color
    t.begin_fill() # Begins filling
    for _ in range(3): # Defines a loop that will run 3 times
        t.fd(size) # Moves Turtle forward as specified by size
        t.rt(-120) # Turns Turtle right by -120 degrees
    t.end_fill() # Ends Filling 

for func, x, y, size, color in draw: # Defines a for loop that expands a tuple into multiple var's
    if func == "c": # Checks the first value for the tuple to check what to draw
        init() # Runs init 
        circle(x, y, size, color) # Runs circle function and puts in selected varibles
    if func == "r": # Checks the first value for the tuple to check what to draw
        init() # Runs init
        rectangle(x, y, size, color) # Runs rectangle function and puts in selected varibles
    if func == "s": # Checks the first value for the tuple to check what to draw
        init() # Runs init
        star(x, y, size, color) # Runs star function and puts in selected varibles
    if func == "t": # Checks the first value for the tuple to check what to draw
        init() # Runs init
        triangle(x, y, size, color) # Runs triangle function and puts in selected varibles
        
t.done() # Tells the Turtle to leave us alone
