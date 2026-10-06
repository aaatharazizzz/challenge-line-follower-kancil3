# Blok setup robot. Dipakai bersama oleh main.py dan kalibrasi.py,
# jadi port dan ukuran roda cukup diubah di satu tempat ini.

from pybricks.hubs import InventorHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor
from pybricks.parameters import Port, Direction
from pybricks.robotics import DriveBase
from pybricks.tools import wait

from perangkat import robot

robot.turn(90)

wait(1000)

robot.turn(90)

wait(1000)

robot.turn(90)

wait(1000)

robot.turn(90)

wait(1000)