import time
import board
from src.button import Button
import config
from src.motor import Motor
from src.encoder import Encoder
from src.ir_sensor import IR_sensor
from adafruit_motorkit import MotorKit
import rotaryio
import analogio
from src.robot import Robot
from src.magnetometer import Magnetometer
from src.random_maze_solve import RandomMazeSolve
from src.floodfill import FloodFill
from digitalio import DigitalInOut, Direction, Pull

# Solving Maze Using FloodFill Algorithm:
time.sleep(5)
road_runner = FloodFill()
road_runner.main()
