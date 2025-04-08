"""
This program makes a DJI Tello takeoff do flip in a user speified direction and land.
"""
from djitellopy import Tello # Imports Tello library

flip = input("Direction: ") # Asks user for direction

drone = Tello() # Creates a drone

drone.connect() # Tells drone to connect
drone.takeoff() # Tells drone to takeoff

drone.move_up(100) # Moves drone up so it can flip

drone.flip(flip) # Flips 

drone.land() # Tells drone to land
