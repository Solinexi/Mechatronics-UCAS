"""
This program makes a DJI Tello takeoff and land.xs
"""
from djitellopy import Tello # Imports Tello library

drone = Tello() # Creates a drone

drone.connect() # Tells drone to connect
drone.takeoff() # Tells drone to takeoff

drone.move_right(330) # Moves right
drone.move_forward(350) # Fowards
drone.move_up(80) # Up
drone.move_back(70) # Back
drone.move_up(80) # Up
drone.move_forward(70) # Foward
drone.move_right(350) # Right
drone.move_back(330) # back

drone.land() # Tells drone to land
