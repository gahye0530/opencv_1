import cv2
import numpy as np

# 1차원배열
arr = np.array([5, 10, 15])
print(arr)
print(arr.shape)
print(arr[0])
arr[1] = 50
print(arr)
# 2차원배열
array_2d = np.array([5, 6, 1, 2, 9, 10])
array_2d = array_2d.reshape(3,2)
print(array_2d)

# 2차원배열의 억세스
# 두번째 행 두번째 열의 데이터를 억세스
print(array_2d[1][1])


# 이미지 파일을 컬러(BGR)로 읽어오는 방법
img = cv2.imread('data/images/sample.jpg')
print(img) # 3차원 행렬로 출력된다.
print(img.shape) # 512*512 이 3장있어
print(img.ndim) # 차원 : 3

# 이미지 파일을 그레이스케일로 읽어오는 방법
img2 = cv2.imread('data/images/sample.jpg',flags=0)
print(img2)
print(img2.shape) # 512*512 1장있음
print(img2.ndim) # 차원 : 2





# def main() :
#     pass
# if __name__ =='__main__' : main()