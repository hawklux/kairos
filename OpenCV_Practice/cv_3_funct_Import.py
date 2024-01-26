# cv_3_funct.py 파일의 함수들을 가져다 쓰는 예제 파일

import cv2
from cv_3_funct import ImageProcessor

# 새 객체 생성
imgEditor = ImageProcessor()

# # 원본함수 모두 실행
# imgEditor.run_editing()

# 필요한 함수만 실행
while True:
    ret, frame = imgEditor.capt.read()

    # 원본 이미지
    cv2.imshow("Original2", frame)

    # 20 밝아진 이미지
    brightened = imgEditor.set_brightness(frame, 20)
    cv2.imshow("Brighter2", brightened)

    if cv2.waitKey(1) == ord('q'):
        break

imgEditor.capt.release()
cv2.destroyAllWindows()
