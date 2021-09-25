import serial
import time

arduino_com_port = "COM5"
baud_rate = 9600
serial_port = serial.Serial(arduino_com_port, baud_rate, timeout=1)
start_time = cur_time = time.time()
data = {}
coef = [8.264070477002113,-5.180794628332823]
voltage = 0

while True:
    time_diff = time.time() - start_time
    # if time_diff > 20:
    #     break
    # print(float(serial_port.readline().decode())/1025*5)
    voltage = float(serial_port.readline().decode())*.0049
    print(voltage*coef[0] + coef[1])
    print('\n')
    # data[time_diff] = [serial_port.readline().decode(), (float(serial_port.readline().decode()))*coef[0] + coef[1]]
    # time.sleep(1)

print(data)