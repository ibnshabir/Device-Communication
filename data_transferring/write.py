import serial
import RPi.GPIO as GPIO
from time import sleep


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)


port = serial.Serial('/dev/ttyS0', baudrate= 9600,
                     bytesize = serial.EIGHTBITS,
                     parity = serial.PARITY_NONE,
                     stopbits = serial.STOPBITS_ONE)

GPIO.output(18, GPIO.HIGH)
print("transmitted data")

port.write(b"testing...")
sleep(3)

GPIO.output(18, False)

port.close()