# Pengikut garis PD dengan kecepatan adaptif dan pencarian garis hilang.
# Penjelasan setiap bagian ada di pengikut-garis.md.

from pybricks.tools import wait
from pybricks.parameters import Color, Icon

from perangkat import robot, color_sensor, hub, ultrasonic_sensor, color_sensor_motor

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
FLAG_DISTANCE_TRESHOLD = 400

THRESHOLD = (BLACK + WHITE) / 2
SCALE = 200 / (WHITE - BLACK)

last_error = 0
lost_time = 0

# colorsensor mode: tracking 
hub.display.icon(Icon.CIRCLE)

print(color_sensor_motor.angle())
color_sensor_motor.reset_angle()
color_sensor_motor.run_angle(100, -90)

while True:
    # Tantangan dinding berwarna ditambahkan di sini:
    # cek dinding di depan, baca warnanya, lalu belok sesuai aturan,
    # dan kembali ke garis sebelum loop berlanjut.
    color = color_sensor.color()
    distance = ultrasonic_sensor.distance()

    if(distance < 70) :
        if color == Color.GREEN:
            print("green")
            hub.speaker.beep(500, 100)
        elif color == Color.RED:
            print("red")
            hub.speaker.beep(1000, 200)
        elif color == Color.YELLOW:
            print("yellow")
            hub.speaker.beep(2000, 300)
    wait(LOOP_MS)
