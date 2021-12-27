import cv2
import numpy as np

img_file = 'data/images/sample.jpg'

# opencv로 이미지 열기
# flags의 default값이 cv2.IMREAD_COLOR임 순서는 BGR
image = cv2.imread(img_file, flags=cv2.IMREAD_COLOR)

# 이미지가 정상인지 체크하는 코드
if image is None :
    print('이미지 파일을 열 수 없습니다.')
else :
    print(image.shape)

# opencv 에서는, 이미지를 BGR로 읽어옵니다. 
# 불러온 이미지를 그레이스케일로 변경할 수 있습니다.
# cvt : convert
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("color", image)
cv2.imshow('gray scale',gray_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
# imshow가 실행되었다가 바로 종료됩니다.
# cpu가 imshow를 실행하고 다음코드를 실행하는데 아무코드가 없어서 프로그램이 종료되었다.
# 따라서 우리 눈으로 확인하기 위해서는
# cpu의 코드실행을 잠시 멈추게 해야 한다. 