import cv2 as cv2
from matplotlib import pyplot as plt
import numpy as np
#"Импортируе" фотографию для дальнейшей работы
pic = cv2.imread("variant-4.jpg", cv2.IMREAD_COLOR)
#Смена цветого пространства с RGB на HSV для более гибкой работы с изображением
hsv = cv2.cvtColor(pic, cv2.COLOR_BGR2HSV)

#Диапазон синего цвета в HSV
lower_blue = np.array([100, 50, 50])
upper_blue = np.array([130, 255, 255])

#Порог изображения HSV, чтобы получить только синие цвета
mask = cv2.inRange(hsv, lower_blue, upper_blue)
#Наложение "маски" поверх старого изображения для отображения только синего цвета
blue_pic = cv2.bitwise_and(pic, pic, mask=mask)

#Вывод изображения
cv2.imshow('mask',pic)
cv2.imshow('Only blue channel', blue_pic)
k = cv2.waitKey()
plt.show()
