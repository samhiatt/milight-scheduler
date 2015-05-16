#!/usr/bin/env python
import milight


controller = milight.MiLight({'host': '192.168.42.100', 'port': 8899}, wait_duration=0)
light = milight.LightBulb(['white'])

def dawn():
	controller.send(light.warmness(100))
	controller.send(light.brightness(70))

def sunrise():
        controller.send(light.brightness(100))
        controller.send(light.warmness(0))

def sunset():
        controller.send(light.warmness(100))
        controller.send(light.brightness(100))

def dusk():
        controller.send(light.brightness(20))
        controller.send(light.warmness(0))

