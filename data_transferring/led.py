import RPi.GPIO as GPIO
from time import sleep

pin = 8
GPIO.setwarnings(False)
try:
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin, GPIO.OUT)

    while(True):
        #GPIO.output(pin, True)
        GPIO.output(pin, GPIO.HIGH)
        sleep(1)
        GPIO.output(pin, False)
        sleep(1)
   
   
except KeyboardInterrupt:
    print('Keyboard Interrupt')
    
except:
    print('some error')
    
finally:
    print('clean up')
    GPIO.cleanup()
