import cv2
import numpy as np
from pyzbar.pyzbar import decode

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

while True:
    success, img = cap.read()
    for barcode in decode(img):
        barcode_data = barcode.data.decode("utf-8")
        print(barcode_data)
        points = np.array([barcode.polygon], np.int32)
        points = points.reshape((-1, 1, 2))
        cv2.polylines(img, [points], True, (222, 159, 91), 5)
        point_2 = barcode.rect
        cv2.putText(img, barcode_data, (point_2[0], point_2[1]), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (222, 159, 91), 2)
    
    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break