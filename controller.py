#!/usr/bin/env python
import milight, datetime


controller = milight.MiLight({'host': '192.168.42.100', 'port': 8899}, wait_duration=0)
light = milight.LightBulb(['white'])

def dawn():
	controller.send(light.brightness(30))
	controller.send(light.warmness(70))
	print("%s --- Lights set to dawn." % str(datetime.datetime.now()))

def sunrise():
        controller.send(light.brightness(100))
        controller.send(light.warmness(70))
	print("%s --- Lights set to sunrise." % str(datetime.datetime.now()))

def noon():
        controller.send(light.brightness(100))
        controller.send(light.warmness(0))
	print("%s --- Lights set to noon." % str(datetime.datetime.now()))

def sunset():
        controller.send(light.brightness(100))
        controller.send(light.warmness(100))
	print("%s --- Lights set to sunset." % str(datetime.datetime.now()))

def dusk():
        controller.send(light.brightness(40))
        controller.send(light.warmness(100))
	print("%s --- Lights set to dusk." % str(datetime.datetime.now()))

def night():
        controller.send(light.brightness(10))
        controller.send(light.warmness(100))
	print("%s --- Lights set to night." % str(datetime.datetime.now()))
