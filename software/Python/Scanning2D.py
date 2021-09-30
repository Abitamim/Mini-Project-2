import serial
import numpy as np 
import csv

arduino_com_port = "COM3" #change depending on Arduino
baud_rate = 9600

serial_port = serial.Serial(arduino_com_port, baud_rate, timeout=1)
data = []

rotAngle, voltage = 0, 0
rotAnglePrev = 999

while True:
    if len(data) > 50: #should be greater than # of rotational angles
        break
    #tells the arduino to start reading, only needs to run once but doesn't work
    #when transferred out of loop for unknown reason
    serial_port.write("Start".encode('utf-8'))
    reading = serial_port.readline().decode()
    rotAngle, voltage = reading.split()

    data.append([rotAngle, voltage]) #add new point to list

serial_port.close()

#remove empty arrays
data = [x for x in data if len(x) > 0]

with open("data_2d.csv", "w", newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["Rotational Angle", "Voltage"])
    writer.writerows(data)