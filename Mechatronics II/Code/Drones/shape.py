"""
This program makes a DJI Tello takeoff and land.xs
"""
from djitellopy import Tello # Imports Tello library

s = int(input("Whats the side num?")) # asks for user input for side and assigns to to a varible
l = int(input("Whats the length?")) # asks for user input for length and assigns to to a varible

drone = Tello() # Creates a drone

drone.connect() # Tells drone to connect
drone.takeoff() # Tells drone to takeoff

def shape(s,l): # defines a subroutine to draw a star
    for i in range(s):# runs this loop 5 times
        drone.move_forward(l)
        drone.rotate_clockwise(round(360/s))

shape(s,l)
        
drone.land() # Tells drone to land
