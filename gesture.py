#gesture.py

import serial
import pyautogui

Arduino_Serial = serial.Serial('/dev/ttyACM0',9600)
print('start')

while 1:
	incoming_data = str(Arduino_Serial.readline())
	print(incoming_data)

	if 'previous' in incoming_data:     
		pyautogui.press('space')
		print("previous")


	incoming_data = "";
