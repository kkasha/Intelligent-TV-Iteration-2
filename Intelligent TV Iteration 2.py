#!/usr/bin/env python

import RPi.GPIO as GPIO
import time
import os

GPIO.setmode(GPIO.BOARD)
#flag is set to 1=play and 0=pause
flag = 1

def setup():
	#GPIO.setmode(GPIO.BOARD)
	GPIO.setup(13, GPIO.OUT)
	GPIO.setup(16, GPIO.IN)

def distance():
	GPIO.output(13, 0)
	time.sleep(0.000002)

	GPIO.output(13, 1)
	time.sleep(0.00001)
	GPIO.output(13, 0)

	
	while GPIO.input(16) == 0:
		a = 0
	time1 = time.time()
	while GPIO.input(16) == 1:
		a = 1
	time2 = time.time()

	during = time2 - time1
	return during * 340 / 2 * 100

def loop():
	while True:
		dis = distance()
		if dis < 30:
			if flag !=0:
                        	os.system("irsend SEND_ONCE TCL_ROKU_TV KEY_PAUSE")
				global flag
				flag = 0
		else:
			if flag !=1:
				os.system("irsend SEND_ONCE TCL_ROKU_TV KEY_OK")
				global flag
				flag = 1	
		print dis, 'cm'
		print flag
		print ''
		time.sleep(1)

def destroy():
	GPIO.cleanup()

if __name__ == "__main__":
	setup()
	try:
		loop()
	except KeyboardInterrupt:
		destroy()
