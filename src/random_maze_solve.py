import board
import config
from src.robot import Robot
from src.encoder import Encoder
import rotaryio
import random

TURN_LEFT = 1
TURN_RIGHT = 2

class RandomMazeSolve:

    def __init__(self):
        encL = rotaryio.IncrementalEncoder(config.l_encA, config.l_encB)
        encR = rotaryio.IncrementalEncoder(config.r_encA, config.r_encB)
        self.robot = Robot(encL, encR)

    def maze_solver(self):
        while True:
            forward_count = 0
            while ((not self.robot.wallFront()) and (forward_count < 5)):
                self.robot.forward()
                forward_count += 1

            if ((self.robot.wallLeft()) and (not self.robot.wallRight())):
                self.robot.turnRight()
                forward_count=0
            elif ((self.robot.wallRight()) and (not self.robot.wallLeft())):
                self.robot.turnLeft()
                forward_count=0
            else:
                direction = random.randrange(1, 3)
                if (direction == 1):
                    self.robot.turnLeft()
                    forward_count=0
                else:
                    self.robot.turnRight()
                    forward_count=0
