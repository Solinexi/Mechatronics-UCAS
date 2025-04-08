"""
This program makes a DJI Tello takeoff and land.xs
"""
from djitellopy import Tello # Imports Tello library

drone = Tello() # Creates a drone

drone.connect() # Tells drone to connect
drone.takeoff() # Tells drone to takeoff

drone.move_forward(70)
drone.move_left(70)
drone.move_back(70)
drone.move_right(70)

drone.land() # Tells drone to land
