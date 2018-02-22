# Copyright (c) 2018 Hal Martin
# This is free software, licensed under the Apache LIcense 2.0
# See /LICENSE for more information

# This file is executed on every boot (including wake-boot from deepsleep)
import gc
gc.collect()

# connect to WiFi
import network
sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)
sta_if.connect("MySSID","P4ssw0rd!")

from time import sleep
while not sta_if.isconnected():
    sleep(1)

# disable the AP if we are connected to a station
ap_if = network.WLAN(network.AP_IF)
ap_if.active(False)

from tempsens import TempSensReport
TempSensReport()
