from RobokitRS import *
import time as t
rs = RobokitRS.RobokitRS()
rs.port_open("com3")
print("연결완료")

# rs.set_mecanumwheels_drive_front(15,1)
# t.sleep(1)
rs.set_mecanumwheels_drive_front(15,1)
t.sleep(1)
# rs.set_mecanumwheels_drive_stop(1)
# t.sleep(1)