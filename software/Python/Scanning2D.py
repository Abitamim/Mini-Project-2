import serial
import numpy as np 
import csv

arduino_com_port = "COM3"
baud_rate = 9600
background = 20

serial_port = serial.Serial(arduino_com_port, baud_rate, timeout=1)
data = []

rotAngle, voltage = 0, 0
rotAnglePrev = 999

while True:
    if len(data) > 50:
        break
    serial_port.write("Start".encode('utf-8'))
    reading = serial_port.readline().decode()
    try:
        rotAngle, voltage = reading.split()
        if rotAnglePrev != rotAngle:
            print(rotAngle)
            rotAnglePrev = rotAngle
        data.append([rotAngle, voltage])
    except:
        pass

serial_port.close()

data = [x for x in data if len(x) > 0]

with open("data_2d.csv", "w", newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["Rotational Angle", "Voltage"])
    writer.writerows(data)