# https://www.raspberrypi.com/documentation/accessories/camera.html
# install picamera library: https://picamera.readthedocs.io/en/release-1.13/install.html

from picamera import PiCamera
from time import sleep
camera = PiCamera()
camera.start_preview(alpha=192)
sleep(1)
camera.capture("/home/pi/Desktop")