"""
This program makes a DJI Tello takeoff and land.xs
"""
from djitellopy import Tello # Imports Tello library

# Creates our tuple of where to fly
shufly = ((200, 90, 30),
          (200, 90, 20),
          (200, 90, 30),
          (200, 90, 20))

drone = Tello() # Creates a drone

drone.connect() # Tells drone to connect
drone.takeoff() # Tells drone to takeoff

for dis, ang, ass in shufly:
    drone.move_forward(dis) # Moves forward 50
    drone.rotate_clockwise(ang) # Turns 90
    drone.move_up(ass) # Flips user defined

drone.land() # Tells drone to land
