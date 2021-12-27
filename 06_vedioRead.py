import cv2
import numpy as np

# FPS : Frame Per Second(1초당 몇장의 사진으로 구성되어 있나)

cap = cv2.VideoCapture('data/videos/chaplin.mp4')
if cap.isOpened() == False :
    print('비디오 파일을 여는데 실패했습니다.')
else :
    # 반복문으로 구성한다.
    # 동영상은 여러개의 사진으로 되어있기 때문에 시작부터 끝까지 imshow를 반복해서 화면에 출력해주면
    # 이것이 바로 동영상 플레이이다.
    while cap.isOpened() :
        ret, frame = cap.read()
        if ret == True :
            cv2.imshow('Video', frame)
            # 동영상이 플레이 하는 동안 멈추고 싶을땐 esc키를 눌러서 멈추도록 코딩
            if cv2.waitKey(25) & 0xFF == 27 : break
        else :
            break

    cap.release()
    cv2.destroyAllWindows()

