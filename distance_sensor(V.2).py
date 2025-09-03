from arduino import *
from arduino_alvik import ArduinoAlvik
import time

alvik = ArduinoAlvik()

def setup():
    alvik.begin()
    time.sleep(1)

def loop():
    # ð¡ Ruwe afstandsmetingen ophalen
    left, cleft, center, cright, right = alvik.get_distance()

    # ð Afronden op dichtstbijzijnde 5 cm
    sensors = [left, cleft, center, cright, right]
    sensors = [round(val / 4) * 4 for val in sensors]

    # ð« Filter: negeer alles â¥ 50 cm
    sensors = [val if val < 25 else 0 for val in sensors]
    left, cleft, center, cright, right = sensors

    print(f"{left} | {cleft} | {center} | {cright} | {right}")
    time.sleep(0.1)

    # ¨ Check op obstakel binnen 5 cm
    if any(val <= 8 and val > 0 for val in sensors):
        alvik.set_wheels_speed(30, -30)  # Snelle draai
        return

    # ð Grootste waarde en verschil bepalen
    max_val = max(sensors)
    others = [v for v in sensors if v != max_val and v > 0]
    min_val = min(others) if others else max_val
    diff = max_val - min_val

    # ð¤ Bewegingslogica
    if max_val == left and diff >= 8:
        alvik.set_wheels_speed(-40, 40)
    elif max_val == cleft and diff >= 8:
        alvik.set_wheels_speed(0, 45)
    elif max_val == center and diff >= 8:
        alvik.set_wheels_speed(40, 40)
    elif max_val == cright and diff >= 8:
        alvik.set_wheels_speed(45, 0)
    elif max_val == right and diff >= 8:
        alvik.set_wheels_speed(40, -40)
    else:
        alvik.set_wheels_speed(60, 60)

def cleanup():
    alvik.stop()

# ð Hoofdlus
try:
    setup()
    while True:
        loop()
except KeyboardInterrupt:
    cleanup()
