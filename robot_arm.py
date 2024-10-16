from RobokitRS import *
import time as t
rs = RobokitRS.RobokitRS()
rs.port_open("com3")
# - = 안 + = 밖
#max = 110 deg
# num = range(-100,-10,10)
# inNum = range(10,-110,10)
# for i in num:
#     rs.servo_write(13, i)
#     t.sleep(1)

# cirAngle = range(-80,80,10)
# for i in cirAngle:
#     rs.servo_write(2,i)
#     t.sleep(1)

# while True:
#     rs.servo_write(2, 80)
#     t.sleep(1)
#     rs.servo_write(2, -80)
#     t.sleep(1)

# while True:    
#     rs.servo_write(4,120)
#     t.sleep(1)
#     rs.servo_write(4,60)
#     t.sleep(1)
# rs.servo_write(12,50)
# t.sleep(1)