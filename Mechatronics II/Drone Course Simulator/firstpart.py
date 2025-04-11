from Drone_Course_Simulator import Drone

tello = Drone("Task 1", (1300, 700), -90)
tello.forward(100)
tello.curve(70, -70, 0, 140, 0, 10)
tello.launch()
