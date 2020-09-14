#!/usr/bin/env python3

import os
import sys
import random

chancePath = "/home/pi/Monopoly/Chance/"

def chance():
    print(chancePath + random.choice(os.listdir("/home/pi/Monopoly/Chance/")))
  
chance()
