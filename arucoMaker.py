from RoboCam.robocam import *
import time as t
rCam = RoboCam()
#rCam.WebcamStreamInit()  #웹캠 카메라 스트림 초기화
# rCam.WebcamStream()      #웹캠 카메라 스트림 시작
rCam.CameraStreamInit()  #무선 카메라 스트림 초기화
rCam.CameraStream()      #카메라 스트림 시작
rCam.ArucoDetectorInit()  #마커감지 초기화
rCam.ArucoDetectorStart() #마커감지 시작
t.sleep(4)
roboId = rCam.GetArucoId()
if roboId == 0:
    print('이쓰')
elif roboId == 1:
    print("이")
elif roboId == 2:
    print('승')
elif roboId == 3:
    print('규')
else:
    print('그러니라')
print("종료")

