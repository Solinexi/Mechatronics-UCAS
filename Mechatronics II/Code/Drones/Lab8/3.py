"""
This program makes a DJI Tello takeoff and land.xs
"""
from djitellopy import Tello # Imports Tello library

# Makes our circle pattern varibles
x1 = (70,70,70,70,)
y1 = (70,70,70,70,)
z1 = (0,0,0,0,)
x2 = (140,140,140,140,)
y2 = (0,0,0,0,)
z2 = (0,0,0,0,)
s = (60,60,60,60,)

drone = Tello() # Creates a drone

drone.connect() # Tells drone to connect
drone.takeoff() # Tells drone to takeoff

for x1, y1, z1, x2, y2, z2, speed in zip(x1, y1, z1, x2, y2, z2, s): # For loop for drone
    drone.curve_xyz_speed(x1, y1, z1, x2, y2, z2, speed) # Runs curve command

drone.rotate_clockwise(180) # signals done 
    
drone.land() # Tells drone to land
