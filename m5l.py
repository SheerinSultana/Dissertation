import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(16,GPIO.OUT)
GPIO.setwarnings(False)
z = GPIO.PWM(16,50)
file = open("/home/pi/Documents/values/m5.txt","r")
m = file.read()
file.close()
n = float(m)
n = n - 0.4
if (n<2):
    n = 2
s = str(n)
file = open("/home/pi/Documents/values/m5.txt","w")
file.write(s)
file.close()
z.start(n)
time.sleep(0.5)
