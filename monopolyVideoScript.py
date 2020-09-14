#! usr/bin/env python3

import RPi.GPIO as GPIO
import os
import sys
from subprocess import Popen
import random



GPIO.setmode(GPIO.BCM)

GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Define Video Locations
movie1 = ("/home/pi/Monopoly/movie1.mp4")
movie2 = ("/home/pi/Monopoly/movie2.mp4")

chancePath = "/home/pi/Monopoly/Chance/"

def chance():
	chance = random.choice(os.listdir("/home/pi/Monopoly/Chance/"))

chest = random.choice(os.listdir("/home/pi/Monopoly/Chest/"))


# Set States
last_state1 = True
last_state2 = True
last_state3 = True
last_state4 = True

input_state1 = True
input_state2 = True
input_state3 = True
input_state4 = True

quit_video = True
player = False

def loop():
	while True:
		#Read states of inputs
		input_state1 = GPIO.input(17)
		input_state2 = GPIO.input(18)
		input_state3 = GPIO.input(27)
		input_state4 = GPIO.input(22)
		quite_video = GPIO.input(24)

		#If GPIO(17) is shorted to ground
		if input_state1 != last_state1:
			if (player and not input_state1):
				os.system('killall omxplayer.bin')
				omxc = Popen(['omxplayer', '-b', movie1])
				player = True
			elif not input_state1:
				omxc = Popen(['omxplayer', '-b', movie1])
				player = True
		
		#If GPIO(18) is shorted to ground
		elif input_state2 != last_state2:
			if (player and not input_state2):
				os.system('killall omxplayer.bin')
				omxc = Popen(['omxplayer', '-b', movie2])
				player = True
			elif not input_state2:
				omxc = Popen(['omxplayer', '-b', movie2])
				player = True
				
		#If GPIO(27) is shorted to ground
		elif input_state3 != last_state3:
			if (player and not input_state3):
				os.system('killall omxplayer.bin')
				omxc = Popen(['omxplayer', '-b', chancePath + chance])
				player = True
			elif not input_state3:
				omxc = Popen(['omxplayer', '-b', chancePath+ chance])
				player = True
				
				
		#If GPIO(22) is shorted to ground		
		elif input_state4 != last_state4:
			if (player and not input_state4):
				os.system('killall omxplayer.bin')
				omxc = Popen(['omxplayer', '-b', chest])
				player = True
			elif not input_state4:
				omxc = Popen(['omxplayer', '-b', chest])
				player = True

			
				

		#If omxplayer is running and NO GPIO are shorted to ground
		elif (player and input_state1 and input_state2):
			os.system('killall omxplayer.bin')
			player = False

		#GPIO(24) to close omxplayer manually - used during debug
		if quit_video == False:
			os.system('killall omxplayer.bin')
			player = False

		#Set last_input states
		last_state1 = input_state1
		last_state2 = input_state2 
		last_state3 = input_state3
		last_state4 = input_state4

def main():
	videos()

if __name__ == '__main__':
    main()
