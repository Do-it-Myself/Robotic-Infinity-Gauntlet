import serial
import time

LEDserial = serial.Serial('COM6', 9600)
LEDserial.timeout = 1

while True:
    i = input("Input: ").strip()
    LEDserial.write(i.encode())
    time.sleep(0.1)
    print(LEDserial.readline().decode('utf-8'))