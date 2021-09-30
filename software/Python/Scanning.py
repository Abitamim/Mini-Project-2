import serial
import numpy as np 
import csv

arduino_com_port = "COM3" #change depending on Arduino
baud_rate = 9600

serial_port = serial.Serial(arduino_com_port, baud_rate, timeout=1)
data = [[]]

rotAngle, tiltAngle, voltage = 0, 0, 0
rotAnglePrev = 999

while True:
    if len(data) > 50: #should be greater than # of rotational angles
        break
    #tells the arduino to start reading, only needs to run once but doesn't work
    #when transferred out of loop for unknown reason
    serial_port.write("Start".encode('utf-8'))
    reading = serial_port.readline().decode()
    try: 
        #will error out when moving to new rotational angle because empty line
        #will be printed, so line cannot be split
        tiltAngle, rotAngle, voltage = reading.split()
        if rotAnglePrev != rotAngle: #for debugging, will print new rotational angle
            print(rotAngle)
            rotAnglePrev = rotAngle
        data[-1].append([rotAngle, tiltAngle, voltage]) #add new point to list
    except:
        #create new array every new rotation
        data.append([]) 

serial_port.close()

#remove empty arrays
data = [x for x in data if len(x) > 0]

#turn into array of lists for each individual point
flat_data = [x for sublist in data for x in sublist]

#save to file
with open("data.csv", "w", newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["Rotational Angle", "Tilt Angle", "Voltage"])
    writer.writerows(flat_data)