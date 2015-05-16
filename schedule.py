#!/usr/bin/env python
import datetime, os
from astral import Astral
import sched, time
import milight
import controller

logfile = open(os.path.join(os.path.dirname(os.path.realpath(__file__)),'schedule.log'),'a')

a = Astral()
a.solar_depression = 'civil'

city_name = 'San Francisco'
city = a[city_name]

today = datetime.date.today()
sun = city.sun(date=today, local=True)

logfile.write("%s --- %s\n" % (city_name,str(datetime.datetime.now())))

def dawn():
	controller.dawn()
	logfile.write("%s --- Lights set to dawn.\n" % str(datetime.datetime.now()))
	logfile.flush()

def sunrise():
	controller.sunrise()
	logfile.write("%s --- Lights set to sunrise.\n" % str(datetime.datetime.now()))
	logfile.flush()

def noon():
	controller.noon()
	logfile.write("%s --- Lights set to noon.\n" % str(datetime.datetime.now()))
	logfile.flush()

def sunset():
	controller.sunset()
	logfile.write("%s --- Lights set to sunset.\n" % str(datetime.datetime.now()))
	logfile.flush()

def dusk():
	controller.dusk()
	logfile.write("%s --- Lights set to dusk.\n" % str(datetime.datetime.now()))
	logfile.flush()

def night():
	controller.night()
	logfile.write("%s --- Lights set to night.\n" % str(datetime.datetime.now()))
	logfile.flush()

def getEpoch(datetime):
	return int(datetime.strftime("%s"))

s = sched.scheduler(time.time, time.sleep)
s.enterabs(getEpoch(sun['dawn']), 1, dawn, ())
logfile.write("Scheduled dawn for    %s.\n" % str(sun['dawn']))
s.enterabs(getEpoch(sun['sunrise']), 1, sunrise, ())
logfile.write("Scheduled sunrise for %s.\n" % str(sun['sunrise']))
s.enterabs(getEpoch(sun['noon']), 1, noon, ())
logfile.write("Scheduled noon for    %s.\n" % str(sun['noon']))
s.enterabs(getEpoch(sun['sunset']), 1, sunset, ())
logfile.write("Scheduled sunset for  %s.\n" % str(sun['sunset']))
s.enterabs(getEpoch(sun['dusk']), 1, dusk, ())
logfile.write("Scheduled dusk for    %s.\n" % str(sun['dusk']))
nighttime = sun['dusk']+datetime.timedelta(hours=1)
s.enterabs(getEpoch(nighttime), 1, night, ())
logfile.write("Scheduled night for   %s.\n" % str(nighttime))

s.run()

secs = (nighttime-datetime.datetime.now(nighttime.tzinfo)).total_seconds()+1
if secs>100000:
	logfile.write("%s --- Sleeping for %s seconds.\n" % (str(datetime.datetime.now()),secs))
	logfile.flush()
	time.sleep(secs)

logfile.write("%s --- Sun's down. Done.\n" % str(datetime.datetime.now()))
logfile.close()
