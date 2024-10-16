from RobokitRS import *
import time as t
from RoboCam.robocam import *
rs = RobokitRS.RobokitRS()
rCam = RoboCam()
rs.port_open("com3")
rCam.CameraStreamInit()
rCam.CameraStream()  
rCam.SketchDetectorInit()
rCam.SketchDetectorStart()

# 
# while True:
#     print("==============")
#     ins = input("사용하실 기능을 선택해주세요: ")
#     if ins == '1':
#         var = input("원하시는 번호를 선택해주세요: ")
#         for i in range(3):
#             t.sleep(1)
#             print(f"촬영시작{3-i}초전")
#         rCam.SketchCapture(var, captureCount=5,path='C:/drink_machine')
#     elif ins == '2':
#         rCam.TrainSketchData(sketchPath='C:/drink_machine')
#     elif ins == 'q':
#         break
#     else:
#         print("잘못 입력하셨습니다.")

while True:
    rs.set_mecanumwheels_drive_front(15,1)
    t.sleep(1)
    rs.sonar_begin(2)
    sonar = rs.sonar_read(2)
    print(sonar)
    t.sleep(0.5)
    if sonar < 15:
        rs.set_mecanumwheels_drive_stop()
    break

rCam.TrainSketchData(sketchPath='C:/drink_machine')
while(True):
    name = rCam.GetSketchNames()
    if name == None or name[0] == 'Sketch':
        continue
    elif name[0] == '1':
        rs.set_mecanumwheels_drive_right(15,1)
        t.sleep(1)
        rs.set_mecanumwheels_drive_stop()
        t.sleep(1)
    elif name[0] == '2':
        rs.set_mecanumwheels_drive_stop()
        t.sleep(1)
        rs.servo_write(13,-50)
        t.sleep(1)
        rs.servo_write(12,30)
        t.sleep(1)
        rs.servo_write(13,-110)
        t.sleep(1)
        rs.servo_write(12,90)
        t.sleep(1)
        rs.set_mecanumwheels_drive_stop()
        t.sleep(1)
        break
    t.sleep(1)

while True:
        rs.set_mecanumwheels_drive_back(15,1)
        t.sleep(2)
        rs.set_mecanumwheels_rotate_right(15,1)
        t.sleep(1)
        rs.servo_write(12,30)
        t.sleep(1)
        rs.servo_write(13,-50)
        t.sleep(1)
        rs.set_mecanumwheels_drive_front(10,1)
        t.sleep(1)
        rs.set_mecanumwheels_drive_stop()
        t.sleep(1)
        break