# https://www.raspberrypi.com/documentation/accessories/camera.html
# install picamera library: https://picamera.readthedocs.io/en/release-1.13/install.html

from picamera import PiCamera
from time import sleep
camera = PiCamera()
camera.start_preview()
sleep(5)
camera.capture("/home/pi/Desktop/image.jpg")
camera.stop_preview()