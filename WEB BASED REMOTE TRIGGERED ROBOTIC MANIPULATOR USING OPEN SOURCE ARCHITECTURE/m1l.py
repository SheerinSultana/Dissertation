import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(35,GPIO.OUT)
GPIO.setwarnings(False)
z = GPIO.PWM(35,50)
file = open("/home/pi/Documents/values/m1.txt","r")
m = file.read()
file.close()
n = float(m)
n -= 0.4
if (n<2):
    n = 2
s = str(n)
file = open("/home/pi/Documents/values/m1.txt","w")
file.write(s)
file.close()
z.start(n)
time.sleep(0.5)
