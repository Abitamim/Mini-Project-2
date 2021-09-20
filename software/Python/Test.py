import serial
import time

arduino_com_port = "COM4"
baud_rate = 9600
serial_port = serial.Serial(arduino_com_port, baud_rate, timeout=1)
start_time = cur_time = time.time()
data = {}

while True:
    time_diff = time.time() - start_time
    if time_diff > 5:
        break
    print(serial_port.readline().decode())
    data[time_diff] = serial_port.readline().decode()
    
print(data)