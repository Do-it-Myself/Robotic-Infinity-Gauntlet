import serial
import time

LEDserial = serial.Serial('COM6', 9600)
LEDserial.timeout = 1

while True:
    i = input("Input: ").strip()
    
    if i == "Done":
        print('finished')
        break
    
    LEDserial.write(i.encode())
    time.sleep(0.5)
    print(LEDserial.readline().decode('ascii'))

LEDserial.close()