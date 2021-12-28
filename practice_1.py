import cv2
import numpy as np
from utils import get_four_points

image_1 = cv2.imread('data/images/first-image.jpg')
image_ts = cv2.imread('data/images/times-square.jpg')

point_src = get_four_points(image_1)
point_dst = get_four_points(image_ts)

print(point_src)
print(point_dst)

matrix, status = cv2.findHomography(point_src, point_dst)



cv2.waitKey(0)
cv2.destroyAllWindows()