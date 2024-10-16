from RoboCam.robocam import *
import time as t
rCam = RoboCam()
#rCam.WebcamStreamInit()  #웹캠 카메라 스트림 초기화
# rCam.WebcamStream()      #웹캠 카메라 스트림 시작
rCam.CameraStreamInit()  #무선 카메라 스트림 초기화
rCam.CameraStream()      #카메라 스트림 시작
rCam.SketchDetectorInit()  #얼굴감지 초기화
rCam.SketchDetectorStart() #얼굴감지 시작
while True:
    print("=====================")
    ins = input("사용할 기능을 입력해주세요: ")
    if ins == '1':
        var = input("저장할 이름을 입력해주세요: ")
        for i in range(3):
            t.sleep(2)
            print(f'촬영시작{3-i}초전')
        rCam.SketchCapture(var, captureCount=5,path='C:/sketch')
    elif ins == '2':
        rCam.TrainSketchData(sketchPath='C:/sketch')
    elif ins == '3':
        var = input("삭제할 이름을 입력해주세요: ")
        rCam.DeleteSketchData(var,sketchPath='C:/sketch')
    elif ins == 'q':
        break
    else:
        print("잘못된 명령어입니다. 다시 입력해주세요")

rCam.TrainSketchData(sketchPath='C:/sketch')
while(True):
    name = rCam.GetSketchNames()
    if name == None or name[0] == 'Sketch':
        continue
    elif name[0] == 'tri':
        print('첫 삼각형')
    elif name[0] == 'triangle':
        print('두번째 삼각형')
    elif name[0] == 'sqaure':
        print('사각형')
    t.sleep(1)