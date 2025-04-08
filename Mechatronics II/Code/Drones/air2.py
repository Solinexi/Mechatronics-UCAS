"""

"""

from tellopy import Tello
from time import sleep

def upflip(): # Defines our upflip function
    drone.move_up(50)
    sleep(1)
    drone.flip("f")
    sleep(1)
    drone.move_down(100)
            
def tri():
    for i in range(3):
        drone.move_forward(50)
        drone.rotate_clockwise(120)
    
drone = Tello()

drone.connect(False)
sleep(1)

drone.takeoff()
sleep(1)

drone.move_up(100)
sleep(1)

drone.keep_alive()

upflip()
sleep(1)

drone.keep_alive()

tri()
sleep(1)

drone.keep_alive()

drone.flip("f")
sleep(1)
drone.flip("b")
sleep(1)

drone.land() # Tells drone to land
