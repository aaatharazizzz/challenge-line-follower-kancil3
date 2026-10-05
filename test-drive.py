# Blok setup robot. Dipakai bersama oleh main.py dan kalibrasi.py,
# jadi port dan ukuran roda cukup diubah di satu tempat ini.

from pybricks.hubs import InventorHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor
from pybricks.parameters import Port, Direction
from pybricks.robotics import DriveBase
from pybricks.tools import wait

hub = InventorHub()
left = Motor(Port.E, Direction.COUNTERCLOCKWISE)
right = Motor(Port.F, Direction.CLOCKWISE)
color_sensor = ColorSensor(Port.D)
ultrasonic_sensor = UltrasonicSensor(Port.C)
color_sensor_motor = Motor(Port.B)

# Ganti dengan hasil kalibrasi robot kalian sendiri,
# lihat bagian 8 dasar-pybricks.md.
robot = DriveBase(left, right, wheel_diameter=56, axle_track=80)

robot.turn(90)

wait(1000)

robot.turn(90)

wait(1000)

robot.turn(90)

wait(1000)

robot.turn(90)

wait(1000)