import serial
import RPi.GPIO as GPIO
import time

pin = 18

GPIO.setwarnings(False)      #  Since using same pin for read and write function, therfore generates a runtime warning

GPIO.setmode(GPIO.BCM)       #  Broadcam pin-numbering scheme

GPIO.setup(pin, GPIO.OUT)    #  pin set to output mode, will send signals

#initial state of the led
print("Testing the pin, press ctrl+c to exit.")

try:
    print("pin set to transmission mode")
    GPIO.output(pin, GPIO.HIGH)  #  pin set to transmission mode
    #time.sleep(5)
    
    port = serial.Serial('/dev/ttyS0', 9600,
                     bytesize = 8, stopbits = 1,
                     parity = serial.PARITY_NONE)
                     

    while True:
        data = input("enter something:  ")
        port.write((data).encode())    #port.write(str(data).encode()) removed the str from it
        port.write(b"... ")
    
except KeyboardInterrupt: #  if ctrl+c pressed, clean exit
    print("Keyboard Interrupt")
    
except:
    print("some error")
    
finally:
    print("cleaning up")
    GPIO.cleanup() # cleanup all GPIO
