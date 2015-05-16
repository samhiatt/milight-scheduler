#!/usr/bin/env python
import datetime, os
from astral import Astral
import sched, time
import milight

logfile = open(os.path.join(os.path.dirname(os.path.realpath(__file__)),'schedule.log'),'a')

a = Astral()
a.solar_depression = 'civil'

city_name = 'San Francisco'
city = a[city_name]

today = datetime.date.today()
sun = city.sun(date=today, local=True)

logfile.write("%s --- %s\n" % (city_name,str(datetime.datetime.now())))
#print('%s\nDawn:    %s\nSunrise: %s\nNoon:    %s\nSunset:  %s\nDusk:    %s' % (city_name,str(sun['dawn']),str(sun['sunrise']),str(sun['noon']),str(sun['sunset']),str(sun['dusk'])))

controller = milight.MiLight({'host': '192.168.42.100', 'port': 8899}, wait_duration=0)
light = milight.LightBulb(['white'])

def dawn():
	controller.send(light.warmness(100))
	controller.send(light.brightness(70))
	logfile.write("%s --- Lights set to dawn.\n" % str(datetime.datetime.now()))
	logfile.flush()

def sunrise():
        controller.send(light.brightness(100))
        controller.send(light.warmness(0))
	logfile.write("%s --- Lights set to sunrise.\n" % str(datetime.datetime.now()))
	logfile.flush()

def sunset():
        controller.send(light.warmness(100))
        controller.send(light.brightness(100))
	logfile.write("%s --- Lights set to sunset.\n" % str(datetime.datetime.now()))
	logfile.flush()

def dusk():
        controller.send(light.brightness(20))
        controller.send(light.warmness(0))
	logfile.write("%s --- Lights set to dusk.\n" % str(datetime.datetime.now()))
	logfile.flush()

s = sched.scheduler(time.time, time.sleep)
s.enterabs(sun['dawn'], 1, dawn, ())
logfile.write("Scheduled dawn for    %s.\n" % str(sun['dawn']))
s.enterabs(sun['sunrise'], 1, sunrise, ())
logfile.write("Scheduled sunrise for %s.\n" % str(sun['sunrise']))
s.enterabs(sun['sunset'], 1, sunset, ())
logfile.write("Scheduled sunset for  %s.\n" % str(sun['sunset']))
s.enterabs(sun['dusk'], 1, dusk, ())
logfile.write("Scheduled dusk for    %s.\n" % str(sun['dusk']))

secs = (sun['dusk']-datetime.datetime.now(sun['dusk'].tzinfo)).seconds
logfile.write("%s --- Sleeping for %s seconds.\n" % (str(datetime.datetime.now()),secs))
logfile.flush()
time.sleep(secs)
logfile.write("%s --- Sun's down. \nDone.\n" % str(datetime.datetime.now()))
logfile.close()
