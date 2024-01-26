#https://www.youtube.com/watch?v=NL7-xm6kA8Y&list=PLgkpDfSY2Bez0l8oyY0UNGusnk1ZFH7On 

import cv2

# 기본 탬플릿
capture = cv2.VideoCapture(0)
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

while True:
    ret, frame = capture.read()
    cv2.imshow("Original", frame)
    if cv2.waitKey(1) == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()
