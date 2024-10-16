from RoboCam.robocam import *
import time as t
rCam = RoboCam()
#rCam.WebcamStreamInit()  #웹캠 카메라 스트림 초기화
# rCam.WebcamStream()      #웹캠 카메라 스트림 시작
rCam.CameraStreamInit()  #무선 카메라 스트림 초기화
rCam.CameraStream()      #카메라 스트림 시작
rCam.FacedetectorInit()  #얼굴감지 초기화
rCam.FacedetectorStart() #얼굴감지 시작
while True:
    ins = input("사용할 기능의 번호를 입력해주세요:")
    if ins == "1":
        var = input("저장할 이름을 입력해주세요 : ")
        for i in range(3):
            t.sleep(2)
            print(f'촬영시작{3-i}초 전')
        rCam.FaceCapture(var,captureCount=20, path='C:/face') #레이블명
    elif ins == '2':
        rCam.TrainFaceData(facePath='C:/face') # 학습시킬 경로 설정
    elif ins == '3':
        var = input("삭제할 이름을 입력해주세요 : ")
        rCam.DeleteFaceData(var,facePath='C:/face') #삭제할 경로 설정
    elif ins == 'q':
        break
    else:
        print("잘못된 명령어입니다. 다시 입력해주세요")