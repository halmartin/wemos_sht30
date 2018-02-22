# Copyright (c) 2018 Hal Martin
# This is free software, licensed under the Apache LIcense 2.0
# See /LICENSE for more information

import urequests
from time import sleep
from machine import Pin, reset
p2 = Pin(2, Pin.OUT)

HOST="wemos-5a0385"
API="myhost.local"
DB="mydb"
LENGTH=60

def TempSensReport():
    from sht30 import SHT30
    sensor = SHT30()
    url = "http://%s:8086/write?db=%s" % (API,DB)
    for i in range(0,LENGTH+1):
        print('Reboot in %d minutes' % (LENGTH-i))
        # turn on the WeMOS LED
	p2.off()
        # measure values
        temperature, humidity = sensor.measure()
        temp = "temp_C,host=%s value=%.02f" % (HOST,temperature)
        hum = "rel_humidity,host=%s value=%.02f" % (HOST,humidity)
        # send to InfluxDB API
        urequests.post(url,data=temp)
        urequests.post(url,data=hum)
        # print on uart for warm fuzzy feeling
        print('Temperature:', temperature, ' C, RH:', humidity, '%')
        # turn off LED
	p2.on()
        sleep(LENGTH)
    # reboot every range*LENGTH
    reset()
