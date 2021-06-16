import serial
import RPi.GPIO as GPIO
import time

pin = 18

GPIO.setwarnings(False)      #  Since using same pin for read and write function, therfore generates a runtime warningd

GPIO.setmode(GPIO.BCM)       #  Broadcam pin-numbering scheme

GPIO.setup(pin, GPIO.OUT)    #  pin set to output mode, will send signals

#initial state of the led
print("Testing the pin, press ctrl+c to exit.")

try:
    print("pin set to receiving mode")
    GPIO.output(pin, GPIO.LOW)  #  pin set to transmission mode
    
    
    port = serial.Serial('/dev/ttyS0', baudrate= 9600,
                     bytesize = serial.EIGHTBITS,
                     parity = serial.PARITY_NONE,
                     stopbits = serial.STOPBITS_ONE)

    
    
    print("ready to receive data")
    
    while True:
        
        rx_data = port.read()
        data_left = port.inWaiting()
        rx_data += port.read(data_left)
        print(rx_data)
       
    
except KeyboardInterrupt: #  if ctrl+c pressed, clean exit
    print("Keyboard Interrupt")
    
except:
    print("some error")
    
finally:
    print("cleaning up")
    GPIO.cleanup() # cleanup all GPIO

