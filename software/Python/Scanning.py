# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import serial
import time
import numpy as np 
import csv

arduino_com_port = "COM3"
baud_rate = 9600
start_time = cur_time = time.time()
data = []
coef = [-25.285041938862830,80.424586008651660]
voltage = 0
measurements = 0
background = 20

serial_port = serial.Serial(arduino_com_port, baud_rate, timeout=1)
measurements = 0
data = [[]]

rotAngle, tiltAngle, distance = 0, 0, 0
rotAnglePrev = 999

while True:
    serial_port.write("Start".encode('utf-8'))
    reading = serial_port.readline().decode()
    # print(reading)
    try:
        tiltAngle, rotAngle, voltage = reading.split()
        if rotAnglePrev != rotAngle:
            print(rotAngle)
            rotAnglePrev = rotAngle
        # print([rotAngle, tiltAngle, voltage])
        data[-1].append([rotAngle, tiltAngle, voltage])
    except:
        print("passing")
        data.append([])
    #     voltage = float(voltage)*coef[0]*.01 + coef[1]
    #     measurements += 1
    #     data[-1].append([tiltAngle, rotAngle, distance])
    # else:
    #     if voltage == 'Done':
    #         break

serial_port.close()

data = [x for x in data if len(x) > 0]

flat_data = [x for sublist in data for x in sublist]

with open("data.csv", "w", newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["Rotational Angle", "Tilt Angle", "Voltage"])
    writer.writerows(flat_data)