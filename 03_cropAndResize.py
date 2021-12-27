import cv2
import numpy as np
# flags = cv2.IMREAD_COLOR랑 같은의미
source = cv2.imread('data/images/sample.jpg',flags=1)
# 가로 : 80%, 세로 : 60%
scaleX = 0.8
scaleY = 0.6
# interpolation(보간법) : 빈 사이를 어떻게 처리할거냐
scaleDown = cv2.resize(source, None, fx=scaleX, fy=scaleY, interpolation=cv2.INTER_LINEAR)
print(scaleDown)
cv2.imshow('original', source)
cv2.imshow('scaled Down', scaleDown)


# 이미지 자르기
crop_img= source[10:200, 150:250]
cv2.imshow('crop img', crop_img)

cv2.waitKey(0)
cv2.destroyAllWindows()