import serial
import time
import numpy as np 

arduino_com_port = "COM5"
baud_rate = 9600
serial_port = serial.Serial(arduino_com_port, baud_rate, timeout=1)
start_time = cur_time = time.time()
data = []
coef = [-25.285041938862830,80.424586008651660]
voltage = 0
measurements = 0
background = 20

while True:
    time_diff = time.time() - start_time        # why is this here?

    serial_port.write("Start".encode('utf-8'))
    voltage = serial_port.readline().decode()
    
    if voltage != '':
        voltage = float(voltage)*coef[0]*.01 + coef[1]
        measurements += 1
        print(voltage)
        data.append(voltage)
    if measurements == 56:
        break

print(data)

sorted = np.reshape(data, (8, ), order = "F")
# boolSorted = sorted < background
# print(boolSorted)