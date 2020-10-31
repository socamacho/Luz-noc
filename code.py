import time
from adafruit_circuitplayground import cp

cp.pixels.auto_write = False
cp.pixels.brightness = 0.5


def scale_range(value):
    return round(value / 320 * 9)


while True:
    peak = scale_range(cp.light)
    print(cp.light)
    print(int(peak))

    for s in range(10):
        if s <= peak:
            cp.pixels[s] = (0, 0, 255)
        else:
            cp.pixels[s] = (0, 0, 0)
    cp.pixels.show()
    time.sleep(0.05)