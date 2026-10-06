# Pengikut garis PD dengan kecepatan adaptif dan pencarian garis hilang.
# Penjelasan setiap bagian ada di pengikut-garis.md.

from pybricks.tools import wait
from pybricks.parameters import Color, Icon

from perangkat import robot, color_sensor, hub, ultrasonic_sensor, color_sensor_motor

# --- hasil pengukuran, ukur ulang dengan kalibrasi.py setiap ganti lintasan atau ruangan ---
BLACK = 9
WHITE = 85

# --- setelan, setel satu per satu ---
LOOP_MS = 10
FLAG_DISTANCE_TRESHOLD = 150

THRESHOLD = (BLACK + WHITE) / 2
SCALE = 200 / (WHITE - BLACK)

last_error = 0
lost_time = 0

# colorsensor mode: tracking 
hub.display.icon(Icon.CIRCLE)

print(color_sensor_motor.angle())
color_sensor_motor.reset_angle()
color_sensor_motor.run_target(100, 0)

while True:
    # Tantangan dinding berwarna ditambahkan di sini:
    # cek dinding di depan, baca warnanya, lalu belok sesuai aturan,
    # dan kembali ke garis sebelum loop berlanjut.
    color = color_sensor.color()
    reflection = color_sensor.reflection()
    hsv = color_sensor.hsv()

    distance = ultrasonic_sensor.distance()

    if(distance <= FLAG_DISTANCE_TRESHOLD) :
        print(f"{color}, reflection {reflection}, hsv {hsv}")
        if color == Color.GREEN:
            hub.speaker.beep(500, 100)
            hub.display.char('G')
        elif color == Color.RED:
            hub.display.char('R')
            hub.speaker.beep(1000, 200)
        elif color == Color.YELLOW:
            hub.display.char('Y')
            hub.speaker.beep(2000, 300)
        else:
            hub.display.char('?')
    else:
        hub.display.char('.')
    wait(LOOP_MS)
