import pandas as pd    
import re

def dataImport(filename):
    global data
    file = filename + '.txt'
    with open(file,'r') as f:
        data = f.read().split('\n')

dataImport('rooms')
given = input('''Enter the req. Data to book a conf. room
               Data Should be Entered in following order
                # People,# Floor,Start Time,End Time: ''').split(',')

def checkAvailability(inpData):
	global availableRooms,finalRoom
	availableRooms = []
	finalRoom = []

	for room in data:
	    room = room.split(',')
	    #print(room)
	    if int(inpData[0]) <= int(room[1]):
	        #available = room[0]
	        #print(room[1])
	        for i in range(2,len(room),2):
	            #print(i)
	            if inpData[2] == room[i] and inpData[3] == room[i+1]:
	                availableRooms.append(room[0])
	                #print(availableRooms)
	prevDiff = 9                
	for room in availableRooms:
	    #print(room)
	    difference = int(room.split('.')[0]) - int(inpData[1])
	    if prevDiff >= difference:
	        prevDiff = difference
	        finalRoom.append(room)
	        #print(room)
	print('Available Room(s) are:')
	for r in finalRoom:
		print(r)

checkAvailability(given)          
        
