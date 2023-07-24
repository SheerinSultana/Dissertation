import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(40,GPIO.OUT)
GPIO.setwarnings(False)
z = GPIO.PWM(40,50)
file = open("/home/pi/Documents/values/m6.txt","r")
m = file.read()
file.close()
n = float(m)
n = n - 0.4
if (n<2.8):
    n = 2.8
s = str(n)
file = open("/home/pi/Documents/values/m6.txt","w")
file.write(s)
file.close()
z.start(n)
time.sleep(0.5)
