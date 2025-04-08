"""
This program makes a DJI Tello takeoff and land.xs
"""
from djitellopy import Tello # Imports Tello library

drone = Tello() # Creates a drone

drone.connect() # Tells drone to connect
drone.takeoff() # Tells drone to takeoff

drone.curve_xyz_speed(30, 40, 0, 30, 30, 10, 60) # Runs curve command

drone.rotate_clockwise(180) # signals done 
    
drone.land() # Tells drone to land
