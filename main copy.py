# Pengikut garis PD dengan kecepatan adaptif dan pencarian garis hilang.
# Penjelasan setiap bagian ada di pengikut-garis.md.

from pybricks.tools import wait
from pybricks.parameters import Icon, Color
from perangkat import robot, hub, color_sensor, ultrasonic_sensor, color_sensor_motor

# --- hasil pengukuran, ukur ulang dengan kalibrasi.py setiap ganti lintasan atau ruangan ---
BLACK = 9
WHITE = 85

# --- setelan, setel satu per satu ---
BASE_SPEED = 150
MIN_SPEED = 60
KP = 0.8
KD = 3.0
LOOP_MS = 10
LOST_MS = 300

FLAG_DISTANCE_TRESHOLD = 200

THRESHOLD = (BLACK + WHITE) / 2
SCALE = 200 / (WHITE - BLACK)

last_error = 0
lost_time = 0

# init at non color sensor mode 

color_sensor_motor.run_target(100, 180)

is_colorscan_mode = False

while True:
    # Tantangan dinding berwarna ditambahkan di sini:
    # cek dinding di depan, baca warnanya, lalu belok sesuai aturan,
    # dan kembali ke garis sebelum loop berlanjut.
    
    distance = ultrasonic_sensor.distance()
    if(distance <= FLAG_DISTANCE_TRESHOLD) :
        is_colorscan_mode = True
        color_sensor_motor.run_target(100, 90)
        robot.stop()
        color = color_sensor.color()
        if color == Color.GREEN:
            print("green")
            hub.speaker.beep(500, 100)
            robot.turn(90)
        elif color == Color.RED:
            print("red")
            hub.speaker.beep(1000, 200)
            robot.turn(-90)
        elif color == Color.YELLOW:
            print("yellow")
            hub.speaker.beep(2000, 300)
            robot.turn(-90)
        else:
            robot.turn(-90)
    else:
        if(is_colorscan_mode):
            is_colorscan_mode = False
            color_sensor_motor.run_target(100, 180)
        error = (color_sensor.reflection() - THRESHOLD) * SCALE
    
        if error > 80:
            lost_time = lost_time + LOOP_MS
        else:
            lost_time = 0
    
        if lost_time > LOST_MS:
            # Garis hilang: berputar ke arah garis terakhir terlihat.
            robot.drive(0, 90 if last_error > 0 else -90)
        else:
            derivative = error - last_error
            speed = BASE_SPEED - (BASE_SPEED - MIN_SPEED) * abs(error) / 100
            robot.drive(speed, KP * error + KD * derivative)
            last_error = error

    wait(LOOP_MS)
