"""
This program makes a DJI Tello takeoff run a figure 8 twice and land
"""
from djitellopy import Tello # Imports Tello library

# Makes our circle pattern
pattern = ((70, -70, 0, 140, 0, 0, 60),
           (-70, 70, 0, -140, 0, 0, 60),
           (-70, 70, 0, -140, 0, 0, 60),
           (70, -70, 0, 140, 0, 0, 60))

drone = Tello() # Creates a drone

drone.connect() # Tells drone to connect
drone.takeoff() # Tells drone to takeoff

for _ in range(2):
    for x1, y1, z1, x2, y2, z2, speed in pattern: # For loop for drone pattern
        drone.curve_xyz_speed(x1, y1, z1, x2, y2, z2, speed) # Runs curve command
    drone.move_up(100)
        
drone.rotate_clockwise(180) # signals done 
    
drone.land() # Tells drone to land
