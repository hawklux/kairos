#   얼굴/눈 인식

import cv2

# OpenCV Python 기본 3줄: 객체(영상 소스, 해상도 설정)
capt = cv2.VideoCapture(0)
capt.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
capt.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# harr cascade 검출기 객체 생성
face_cascade = cv2.CascadeClassifier('cv_env/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml')
# eye_cascade = cv2.CascadeClassifier('cv_env/Lib/site-packages/cv2/data/haarcascade_eye.xml')

# 실행
while True:
    ret, frame = capt.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # scaleFactor를 1에 가깝게 해주면 정확도가 상승하나 시간이 오래걸림
    # minNeighbors를 높여주면 검출률이 상승하나 오탐지율도 상승
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=3, minSize=(20,20))
    # eyes = eye_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=3, minSize=(10,10))
    
    # 바운딩 박스 표시
    if len(faces):
        for x, y, w, h in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2, cv2.LINE_4)
    # if len(eyes):
    #     for x, y, w, h in eyes:
    #         cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 255, 0), 2, cv2.LINE_4)
    cv2.imshow("Original", frame)
    if cv2.waitKey(1) == ord('q'):
        break

capt.release()
cv2.destroyAllWindows()