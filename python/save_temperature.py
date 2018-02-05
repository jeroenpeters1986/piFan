#!/usr/bin/python
import sys
import Adafruit_DHT
import json

sensor = Adafruit_DHT.DHT22
pin = 4

humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

if humidity is not None and temperature is not None:
    data = {'temperature': "{0:0.1f}".format(temperature)}
    with open('/home/pi/pifan/data/curr_temp.json', 'w') as outfile:
        json.dump(data, outfile)
else:
    sys.exit(1)
