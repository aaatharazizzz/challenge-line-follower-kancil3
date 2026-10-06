# Pengikut garis PD dengan kecepatan adaptif dan pencarian garis hilang.
# Penjelasan setiap bagian ada di pengikut-garis.md.

from pybricks.tools import wait, StopWatch
from pybricks.parameters import Icon, Color
from perangkat import robot, hub, color_sensor, ultrasonic_sensor, color_sensor_motor

# --- hasil pengukuran, ukur ulang dengan kalibrasi.py setiap ganti lintasan atau ruangan ---
BLACK = 12
WHITE = 99

# --- setelan, setel satu per satu ---
BASE_SPEED = 300
MIN_SPEED = 0
KP = 0.8
KD = 3.0
LOOP_MS = 10
LOST_MS = 300

SEARCH_REVERSE_SPEED = -40  # mm/s (negative value makes it go backward)
SEARCH_TURN_RATE = 120

# ADDITIONAL CONSTANTS
COLOR_SENSOR_FRONT_ANGLE = 0
COLOR_SENSOR_DOWN_ANGLE = -90

FLAG_DISTANCE_TRESHOLD = 70
# garis lebar 4.5cm / 45 mm
TURN_ARC = 22
PROPER_COLOR_WAIT_MS = 500
# ---

THRESHOLD = (BLACK + WHITE) / 2
SCALE = 200 / (WHITE - BLACK)

last_error = 0
lost_time = 0

# init at non color sensor mode 

color_sensor_motor.run_target(200, COLOR_SENSOR_DOWN_ANGLE)

is_colorscan_mode = False
color_not_found = False
hub.display.icon(Icon.UP)
while True:
    # Tantangan dinding berwarna ditambahkan di sini:
    # cek dinding di depan, baca warnanya, lalu belok sesuai aturan,
    # dan kembali ke garis sebelum loop berlanjut.
    
    distance = ultrasonic_sensor.distance()
    # print(f"dist {distance}")
    if(distance <= FLAG_DISTANCE_TRESHOLD) :
        is_colorscan_mode = True
        if color_not_found == False:
            robot.stop()
        color_sensor_motor.run_target(200, COLOR_SENSOR_FRONT_ANGLE)
        color = color_sensor.color()

        color_not_found = False
        if color == Color.GREEN:
            print("green")
            hub.display.icon(Icon.ARROW_RIGHT)
            hub.speaker.beep(500, 100)
            # robot.turn(90)
            robot.arc(TURN_ARC, 90)
        elif color == Color.RED:
            print("red")
            hub.display.icon(Icon.ARROW_LEFT)
            hub.speaker.beep(1000, 200)
            # robot.turn(-90)
            robot.arc(-TURN_ARC, 90)
        elif color == Color.YELLOW:
            print("yellow")
            hub.display.char('Y')
            hub.speaker.beep(2000, 300)
            # robot.turn(-90)
            robot.arc(-TURN_ARC, 90)
        else:
            color_not_found = True
            hub.display.char('?')
            robot.drive(0, 30)
    else:
        if(is_colorscan_mode):
            is_colorscan_mode = False
            color_sensor_motor.run_target(200, COLOR_SENSOR_DOWN_ANGLE)
            hub.display.icon(Icon.UP)
        error = (color_sensor.reflection() - THRESHOLD) * SCALE
    
        if error > 80:
            lost_time = lost_time + LOOP_MS
        else:
            lost_time = 0
    
        if lost_time > LOST_MS:
            # Garis hilang: berputar ke arah garis terakhir terlihat.
            turn_direction = SEARCH_TURN_RATE if last_error > 0 else -SEARCH_TURN_RATE
            robot.drive(SEARCH_REVERSE_SPEED, turn_direction)
        else:
            derivative = error - last_error
            speed = BASE_SPEED - (BASE_SPEED - MIN_SPEED) * abs(error) / 100
            robot.drive(speed, KP * error + KD * derivative)
            last_error = error

    wait(LOOP_MS)