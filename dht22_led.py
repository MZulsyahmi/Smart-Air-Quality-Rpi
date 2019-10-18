import RPi.GPIO as gpio
import Adafruit_DHT
import time

gpio.setmode(gpio.BCM)
gpio.setup(16, gpio.OUT)

DHT_Sensor = Adafruit_DHT.DHT22
DHT_PIN = 17

while True:
    humidity, temperature = Adafruit_DHT.read(DHT_Sensor, DHT_PIN)
    if humidity and temperature is not None:
        print("Temp={0:0.1f}C   Humidity={1:0.1f}%".format(temperature, humidity))
        if (temperature >= 24):
            gpio.output(16, gpio.HIGH)
            print("Temperature high!\n")
            
        else:
            gpio.output(16, gpio.LOW)
            print("Temperature stable\n")
            
    else:
        print("Sensor failure. Check wiring.");
    time.sleep(5);

