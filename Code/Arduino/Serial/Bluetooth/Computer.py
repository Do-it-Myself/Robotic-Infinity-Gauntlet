import serial
import time

LEDserial = serial.Serial('COM24', 9600)
LEDserial.timeout = 2.6

while True:
    i = input("Input: ").strip()
    LEDserial.write(i.encode())
    time.sleep(0.5)
    print(LEDserial.readline().decode('ascii'))
