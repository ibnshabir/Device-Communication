import serial
import RPi.GPIO as GPIO
from time import sleep

#pin = 18

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
#GPIO.setup(pin, GPIO.OUT)
#GPIO.output(pin, GPIO.LOW)

ser = serial.Serial(port = '/dev/ttyS0',
                    baudrate= 9600,
                    bytesize = serial.EIGHTBITS,
                    parity = serial.PARITY_NONE,
                    stopbits = serial.STOPBITS_ONE)

print("ready to receive data")

while True:
    rx_data =ser.read()
    sleep(2)
    data_left = ser.inWaiting()
    rx_data += ser.read(data_left)
    print(rx_data)
    print("...in reception mode... ")
