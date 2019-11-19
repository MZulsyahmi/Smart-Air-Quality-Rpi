'''
---------------------KRENOVATOR---------------------
  Python for DHT22 + LEDs + Blynk Apps

  The codes is for control and monitor the DHT22
  via Python of Raspberry Pi 3B. The LED were
  used as a trigger component in case the user
  set a condition for the temperature and humidity.
  It is connected to Blynk Apps and can be monitored
  via smartphone anywhere. Internet of Things is a
  success

  Get the code at github
  https://github.com/MZulsyahmi/Smart-Air-Quality-Rpi.git
  
  by M.Zulsyahmi @krenovator
  September 2019
'''

import RPi.GPIO as gpio
import Adafruit_DHT
import time

import BlynkLib

#initialize Blynk
blynk = BlynkLib.Blynk('MG0425GclcOgqa7CiNUjqbS6ufran4tD')

DHT_Sensor = Adafruit_DHT.DHT22
DHT_PIN = 17

gpio.setmode(gpio.BCM)
gpio.setup(16, gpio.OUT)
gpio.setup(6, gpio.OUT)

pwm = gpio.PWM(6, 100)

pwm.start(0)

# @blynk.VIRTUAL_WRITE(1)
# @blynk.VIRTUAL_WRITE(2)
# @blynk.VIRTUAL_WRITE(3)

def my_user_task():
    humidity, temperature = Adafruit_DHT.read_retry(DHT_Sensor, DHT_PIN)
    blynk.virtual_write(1, '{:.1f}'.format(temperature))
    blynk.virtual_write(2, '{:.1f}'.format(humidity))
    if(temperature >= 25):
        blynk.virtual_write(3, 255)
        blynk.virtual_write(4, 0)
    else:
        blynk.virtual_write(3, 0)
        blynk.virtual_write(4, 255)

def blinking():
    gpio.output(6, gpio.HIGH)
    time.sleep(1)
    gpio.output(6, gpio.LOW)
    time.sleep(1)
    
# def rpi():
#     humidity, temperature = Adafruit_DHT.read_retry(DHT_Sensor, DHT_PIN)
#     print("Temp={0:0.1f}C   Humidity={1:0.1f}%".format(temperature, humidity))
#     if (temperature >= 23):
#         gpio.output(16, gpio.HIGH)
#         print("Temperature high!\n")
#         
#     else:
#         gpio.output(16, gpio.LOW)
#         print("Temperature stable\n")
#     time.sleep(5)
    
while True:
    humidity, temperature = Adafruit_DHT.read_retry(DHT_Sensor, DHT_PIN)
    print("Temp={0:0.1f}C   Humidity={1:0.1f}%".format(temperature, humidity))
    
    my_user_task()
    
    if (temperature >= 25):
        gpio.output(16, gpio.HIGH)
        print("Temperature high!\n")
        time.sleep(4)
        
    else:
        gpio.output(16, gpio.LOW)
        pwm.ChangeDutyCycle(10)
        print("Temperature stable\n")
        blinking()
        blinking()
        
    blynk.run()
