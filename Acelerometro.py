import serial
import time
arduino = serial.Serial('COM4', 9600)
while 1:
    time.sleep(2)
    rawString = arduino.readline()
    print(rawString)
    arduino.close()