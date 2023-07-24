import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(38,GPIO.OUT)
GPIO.setwarnings(False)
z = GPIO.PWM(38,50)
file = open("/home/pi/Documents/values/m4.txt","r")
m = file.read()
file.close()
n = float(m)
n = n + 0.6
if (n>12):
    n = 12
s = str(n)
file = open("/home/pi/Documents/values/m4.txt","w")
file.write(s)
file.close()
z.start(n)
time.sleep(1)
