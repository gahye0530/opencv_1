import cv2
import numpy as np

image = cv2.imread('data/images/mark.jpg')
cv2.imshow('img', image)

# 선그리기
imageLine = image.copy()
cv2.line(imageLine, pt1=(322, 179), pt2=(400, 183), color=(255, 0, 255), thickness=3, lineType=cv2.LINE_AA)
cv2.imshow('image Line', imageLine)


# 원그리기
imageCircle = image.copy()
cv2.circle(imageCircle, center=(350, 200), radius=150, color=(255, 0, 0), thickness=3, lineType=cv2.LINE_AA)
cv2.imshow('image circle',imageCircle)

# 타원그리기
imageEllipse = image.copy()
cv2.ellipse(imageEllipse, center=(360, 200), axes=(100, 170), angle = 45, startAngle = 0, endAngle = 360, color = (0, 255, 0), thickness = 2)
cv2.ellipse(imageEllipse, (360, 200), (100, 170), 135, 0, 360, (0, 0, 255), 2)
cv2.imshow('image Ellipse',imageEllipse)

# 사각형 그리기
imageRactangle = image.copy()
cv2.rectangle(imageRactangle, pt1=(208, 55), pt2 = (450, 355), color=(255, 0, 0), thickness=3)
cv2.imshow('image Ractangle', imageRactangle)

# 글자 넣기
imageText = image.copy()
cv2.putText(imageText, 'mark Zuckerburg', org = (205, 50), fontFace = cv2.FONT_HERSHEY_SIMPLEX, fontScale = 1, color = (0, 255, 0), thickness = 2)
cv2.imshow('image Text', imageText)
cv2.waitKey(0)
cv2.destroyAllWindows()
