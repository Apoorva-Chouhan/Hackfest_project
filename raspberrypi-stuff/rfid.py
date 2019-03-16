#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 14 23:36:07 2018

@author: Mrinalini Singh
"""


import csv
import serial
import datetime
import numpy 
    
    # run "ls /dev/tty*" on terminal without arduino connected,
    # then connect the Arduino and run the command again.
    #Check ttyACM*, where * maybe 0 or 1, edit this code accordingly.
baud_rate = 9600 #set baudrate
ser = serial.Serial('/dev/ttyACM2', baud_rate)
    #ser = serial.Serial('/dev/ttyACM1', baud_rate)
if (not ser.readline()):
    print("Connection to Arduino failed")
    exit()
else:
    print("Connection to Arduino succeeded")
 
    
new_file_name = "Log-" + datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")+".csv"
while True:
        serial_data = str(ser.readline())
        serial_data = serial_data.rstrip()
        print(serial_data)

with open(new_file_name, 'w') as data_csv:
    file_writer = csv.writer(data_csv) #this will also save the time attribute
    while True:
        serial_data = str(ser.readline())
        serial_data = serial_data.rstrip()
        cardUID = []
        cardSAK = []
        PICCtype = []
        print(serial_data)
