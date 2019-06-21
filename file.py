#!/usr/bin/python
import sys
import Adafruit_DHT
count=0
f=open("demofile.txt","a")
while(count<=5):
    humidity, temperature = Adafruit_DHT.read_retry(11, 21)
    print 'Temp: {0:0.1f} C  Humidity: {1:0.1f} %'.format(temperature, humidity)
    f.write("temperature=%s humidity=%s\n"%(temperature,humidity))
    count=count+1
f.close()
