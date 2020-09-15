#! usr/bin/env python3

import RPi.GPIO as GPIO
import os
import sys
from subprocess import Popen
import random


GPIO.setmode(GPIO.BCM)
GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_UP)


chancePath = "/home/pi/Monopoly/Chance/"

def chance():
	chancePath + random.choice(os.listdir("/home/pi/Monopoly/Chance/"))

last_state3 = True
input_state3 = True
quit_video = True
player = False

while True:
    input_state3 = GPIO.input(27)
    
    #If GPIO(27) is shorted to ground
    if input_state3 != last_state3:
      if (player and not input_state3):
        os.system('killall omxplayer.bin')
        omxc = Popen(['omxplayer', '-b', str(chance())])
        player = True
      elif not input_state3:
        omxc = Popen(['omxplayer', '-b', str(chance())])
        player = True
		
last_state3 = input_state3         
