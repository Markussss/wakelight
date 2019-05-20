#! /usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import subprocess
from datetime import datetime
from time import sleep


def wakeup(hour, minute):
  print "the time is " + str(hour) + ":" + str(minute) + ". starting wakeup"
  i = 0
  while (i < 30):
    subprocess.call('loginctl unlock-session 2 >> /dev/null', shell=True)
    subprocess.call('xbacklight +5'+ ' >> /dev/null', shell=True)
    subprocess.call('redshift -O ' + str(1000 + ((6000 / 30) * i)) + ' >> /dev/null', shell=True)
    subprocess.call('xdotool mousemove ' + str(i) + " " + str(i) + ' >> /dev/null', shell=True)
    i += 1
    sleep (60)
  subprocess.call('xdg-open /home/markus/wakelight/wakelight.html >> /dev/null', shell=True)

wath = int(sys.argv[1])
watm = int(sys.argv[2])

inith = wath
initm = watm - 30

if (initm < 0):
  inith -= 1
  initm = initm % 60

if (inith == 0):
  inith = 0
if (initm == 0):
  initm = 0

print "wake up at " + str(wath) + ":" + str(watm)
print "starting wakeup process at " + str(inith) + ":" + str(initm)

now = datetime.now().time()

simh = now.hour
simm = now.minute

sleeph = 0
sleepm = 0

while (simm != initm):
  simm += 1
  sleepm += 1
  if (simm == 60): 
    simm = 0
    simh += 1

while (simh != inith):
  simh = (simh + 1) % 24
  sleeph += 1

sleepm += sleeph * 60
sleeps = sleepm * 60


print "going to sleep for " + str(sleeps) + " seconds"
sleep(sleeps)

wakeup(inith, initm)
