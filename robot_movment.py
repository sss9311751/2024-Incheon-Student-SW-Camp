import time as t
import random
from RobokitRS import *
rs = RobokitRS.RobokitRS()
rs.port_open("com3")

# rs.set_rgb_led_color(2,100,100,100)
# rs.set_rgb_led_on(2)
# rs.tone_with_delay(2,76,500)
# rs.tone_with_delay(2,77,500)
# rs.tone_with_delay(2,79,200)
# rs.tone_with_delay(2,76,500)
# rs.tone_with_delay(2,77,500)
# rs.tone_with_delay(2,79,200)
# rs.tone_with_delay(2,76,500)
# rs.tone_with_delay(2,77,500)
# rs.tone_with_delay(2,79,200)
# rs.tone_with_delay(2,79,200)
# rs.tone_with_delay(2,78,500)
# rs.tone_with_delay(2,82,500)
# rs.tone_with_delay(2,85,500)
# time.sleep(5)


#코드 단축을 위해 회전 속도 변수 지정
speed = 5

#함수 선언해서 speed값을 생성
#전진 값
def f():
    rs.motor_write(0,0,speed)
    rs.motor_write(1,1,speed)

#후진 값
def b():
    rs.motor_write(0,1,speed)
    rs.motor_write(1,0,speed)

#우회전 값
def r():
    rs.motor_write(0,1,speed)
    rs.motor_write(1,1,speed)

#좌회전 값
def l():
    rs.motor_write(0,0,speed)
    rs.motor_write(1,0,speed)

#정지 값
def s():
    rs.motor_stop(0)
    rs.motor_stop(1)

# #랜덤 속도 지정
# RanSpeed = range(1,16,1)
# random.randint(RanSpeed)

# #랜덤 속도 값
# def r():
#     rs.motor_write(0,0,RanSpeed)
#     rs.motor_write(1,1,RanSpeed)

# r()
# time.sleep(2)

rs.set_pin_mode(19,RobokitRS.Modes.ANALOG)
#blue = 2, red = 3, white = 1, yellow = 4, green = 5 
while True:
    a_key = rs.sensor_read(0,RobokitRS.SensorType.A_KEYPAD)
    t.sleep(0.1)
    print(a_key)
    t.sleep(0.5)

    if a_key==1:
        s()
    elif a_key==2:
        f()
    elif a_key==3:
        b()
    elif a_key==4:
        l()
    elif a_key==5:
        r()
    else:
        s()

