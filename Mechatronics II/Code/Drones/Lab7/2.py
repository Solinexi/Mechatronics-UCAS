"""
This program makes a DJI Tello takeoff do flip in a user speified direction and land.
"""
from djitellopy import Tello # Imports Tello library

flip = input("Direction: ") # Asks user for direction

drone = Tello() # Creates a drone

drone.connect() # Tells drone to connect
drone.takeoff() # Tells drone to takeoff

drone.move_up(50) # Moves drone up

for _ in range(4): # Makes a for loop to run 4 times
    drone.move_forward(100) # Moves forward 50
    drone.rotate_clockwise(90) # Turns 90
    drone.flip(flip) # Flips user defined

drone.land() # Tells drone to land
