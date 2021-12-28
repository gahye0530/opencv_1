import cv2
import numpy as np
from utils import get_four_points

# 1. 이미지 가져오기
image_1 = cv2.imread('data/images/first-image.jpg') # 600*500 이미지임
image_ts = cv2.imread('data/images/times-square.jpg')
# 2. 타임스퀘어의 이미지에 매칭할 점의 좌표를 구합니다.
point_src = np.array([[0, 0], 
                    [image_1.shape[1],0], 
                    [image_1.shape[1], image_1.shape[0]], 
                    [0, image_1.shape[0]]])
point_dst = get_four_points(image_ts)
# 3. 변환 행렬을 얻어옵니다.
matrix, status = cv2.findHomography(point_src, point_dst)
# 4. 이미지를 변환시킵니다.
image_temp = cv2.warpPerspective(src = image_1, M = matrix, dsize = (image_ts.shape[1],image_ts.shape[0]))
# 5. 변환된 이미지를 화면에 보여줍니다.
cv2.imshow('image_temp', image_temp)

# 6. 변환된 이미지 합성
# fillpolly 합성기본함수
# 우리는 볼록하게 보이기 위해서 fillconvexpoly 사용
# 검정색은 숫자 0
# 두 이미지를 더하면 되도록 만든다.
# 
# 1) 0으로 셋팅 
cv2.fillConvexPoly(img = image_ts, points = point_dst.astype(int), color = 0)
cv2.imshow('Image to 0', image_ts)
# 2) 두 개의 이미지를 더하면 합성이 된다. 
result = image_temp + image_ts
cv2.imshow('result', result)

cv2.waitKey(0)
cv2.destroyAllWindows()