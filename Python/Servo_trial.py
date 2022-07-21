# install gpiozero library: https://gpiozero.readthedocs.io/en/stable/installing.html

from gpiozero import Servo
from time import sleep

servo1 = Servo(25, min_pulse_width = 0.33/1000)
servo2 = Servo(24, min_pulse_width = 0.33/1000)

while True:
    servo1.value = -1
    servo2.value = -1
    sleep(1)
    servo1.value = 1
    servo2.value = 1
    sleep(2)