import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    while True:
        ret, frame = cap.read()

        # Смена цветого пространства с RGB на HSV для более гибкой работы с изображением
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # Диапазон красного цвета в HSV
        red1 = np.array([0, 50, 50])
        red2 = np.array([10, 255, 255])

        mask = cv2.inRange(hsv, red1, red2)  # создаём маску

        # Поиск контуров красного объекта
        contr, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # Конутры метки
        if len(contr) > 0:
            c = max(contr, key=cv2.contourArea)
            ((x, y), radius) = cv2.minEnclosingCircle(c)
            center = (int(x), int(y))
            cv2.circle(frame, center, int(radius), (0, 255, 0), 2)
            
        cv2.imshow('ISHY KRASNUI METKY', frame)
        
        if cv2.waitKey(1):
            break
