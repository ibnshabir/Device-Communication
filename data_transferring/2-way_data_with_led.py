import serial
import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)      #  Since using same pin for read and write function, therfore generates a runtime warning

GPIO.setmode(GPIO.BCM)       #  Broadcam pin-numbering scheme

pin = 18
GPIO.setup(pin, GPIO.OUT)    #  pin set to output mode, will send signals

ser = serial.Serial(port = '/dev/ttyS0',
                    baudrate = 115200,
                    bytesize = 8,
                    stopbits = 1,
                    parity = serial.PARITY_NONE)                  

print("press ctrl+c to exit.\n")
                       
try:                   
    while True:
        GPIO.output(pin, True) #True is GPIO.HIGH
        data = input("transmission mode:  ")
        ser.write(str(data).encode())
        sleep(1)
        while True:
            GPIO.output(pin, False) #False is GPIO.LOW
            print("reception mode")
            rx_data = ser.read()
            data_left = ser.inWaiting()
            while data_left > 0:
                rx_data += ser.read(data_left)
                data_left = ser.inWaiting()
            print(rx_data)
            sleep(1)
            break
   
except KeyboardInterrupt: #  if ctrl+c pressed, clean exit
    print("Keyboard Interrupt")
    
except:
    print("some error")
    
finally:
    print("cleaning up")
    GPIO.cleanup() # cleanup all GPIO
    GPIO.output(pin, False)
    
    
#    Traceback (most recent call last):
#  File "/root/Desktop/testing.py", line 46, in <module>
#    GPIO.output(pin, False)
#RuntimeError: Please set pin numbering mode using GPIO.setmode(GPIO.BOARD) or GPIO.setmode(GPIO.BCM)