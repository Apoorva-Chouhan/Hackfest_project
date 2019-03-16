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
        '''
        #cmp = 'DATA_LINE'
        cmp = "Card Detected:"
        cmp1 = "End Reading"
        if serial_data.find(cmp) != -1 and  serial_data.find(cmp1) != -1: 
            deletestr = "bn'rt ," 
            serial_data = str(ser.readline())
            serial_data = serial_data.rstrip()
            raw_data = serial_data.translate(str.maketrans('', '', deletestr))
            raw_data.rsplit("Card UID: ", 1)
            #cardUID.append(raw_data)
            string_data.append(raw_data)
            serial_data = str(ser.readline())
            serial_data = serial_data.rstrip()
            raw_data1 = serial_data.translate(str.maketrans('', '', deletestr))
            raw_data1.rsplit("Card SAK: ", 1)
            #cardSAK.append(raw_data1)
            string_data.append(raw_data1)
            serial_data = str(ser.readline())
            serial_data = serial_data.rstrip()
            raw_data2 = serial_data.translate(str.maketrans('', '', deletestr))
            raw_data2.rsplit("PICC type: ", 1)
            #PICCtype.append(raw_data2)
            string_data.append(raw_data2)
            
            print(string_data)
                
            file_writer.writerow([str(datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S"))]+string_data)
            
            
        else:
            print(serial_data)'''
