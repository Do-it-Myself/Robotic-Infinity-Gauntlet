import serial
import time

SERVOserial = serial.Serial('COM24', 9600)
SERVOserial.timeout = 1

while True:
    i = input("Input: ").strip()
    SERVOserial.write(i.encode())
    time.sleep(2)
