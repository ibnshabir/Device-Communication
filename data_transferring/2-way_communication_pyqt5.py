from PyQt5.QtCore import QCoreApplication, QIODevice
#from PyQt5.QtSerialPort import QSerialPort
import sys

import serial
import RPi.GPIO as GPIO
from time import sleep

class RS485Bus:
    def __init__(self):
        
        self.ser = serial.Serial(port = '/dev/ttyS0',
                                        baudrate = 115200,
                                        bytesize = 8,
                                        stopbits = 1,
                                        parity = serial.PARITY_NONE)   
        self.pin = 18
        GPIO.setwarnings(False)      #  Since using same pin for read and write function, therfore generates a runtime warning
        GPIO.setmode(GPIO.BCM)       #  Broadcam pin-numbering scheme
        GPIO.setup(self.pin, GPIO.OUT)    #  pin set to output mode, will send signals

    def run(self):
        print("press ctrl+c to exit.\n")
        try:                   
            while True:
                GPIO.output(self.pin, True) #True is GPIO.HIGH
                data = input("transmission mode:  ")
                self.ser.write(str(data).encode())
                sleep(1)
                while True:
                    GPIO.output(self.pin, False) #False is GPIO.LOW
                    print("reception mode")
                    rx_data = self.ser.read()
                    data_left = self.ser.inWaiting()
                    while data_left > 0:
                        rx_data += self.ser.read(data_left)
                        data_left = self.ser.inWaiting()
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
            GPIO.output(self.pin, False)
    

app = QCoreApplication(sys.argv)
bus = RS485Bus()
bus.run()
sys.exit(app.exec())