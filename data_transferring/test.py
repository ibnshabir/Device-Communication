import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)
try:
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(18, GPIO.OUT)

    while(True):
        GPIO.output(18, True)
        sleep(1)
        GPIO.output(18, False)
        sleep(1)
        
except KeyboardInterrupt:
    print('Keyboard Interrupt')
    
except:
    print('some error')
    
finally:
    print('clean up')
    GPIO.cleanup()
    