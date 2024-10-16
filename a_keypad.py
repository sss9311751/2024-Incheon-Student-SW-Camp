import time as t
from RobokitRS import *
rs = RobokitRS.RobokitRS()
rs.port_open("com3")
rs.set_pin_mode(19,RobokitRS.Modes.ANALOG)
#blue = 2, red = 3, white = 1, yellow = 4, green = 5 
while True:
    a_key = rs.sensor_read(5,RobokitRS.SensorType.A_KEYPAD)
    print(a_key)
    t.sleep(0.5)