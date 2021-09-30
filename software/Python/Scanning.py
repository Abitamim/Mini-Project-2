import serial
import numpy as np 
import csv

arduino_com_port = "COM3"
baud_rate = 9600
background = 20

serial_port = serial.Serial(arduino_com_port, baud_rate, timeout=1)
data = [[]]

rotAngle, tiltAngle, voltage = 0, 0, 0
rotAnglePrev = 999

while True:
    if len(data) > 50:
        break
    serial_port.write("Start".encode('utf-8'))
    reading = serial_port.readline().decode()
    try:
        tiltAngle, rotAngle, voltage = reading.split()
        if rotAnglePrev != rotAngle:
            print(rotAngle)
            rotAnglePrev = rotAngle
        data[-1].append([rotAngle, tiltAngle, voltage])
    except:
        data.append([])

serial_port.close()

data = [x for x in data if len(x) > 0]

flat_data = [x for sublist in data for x in sublist]

with open("data.csv", "w", newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["Rotational Angle", "Tilt Angle", "Voltage"])
    writer.writerows(flat_data)