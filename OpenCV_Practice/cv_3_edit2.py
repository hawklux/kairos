# 영상 조정 코드 (색상, 밝기, 대비)

import cv2
import numpy as np

# 1. 색상 변경 함수 설정
def color_filter(img, color, scale): # 이미지, 색상, 비율
    dst = np.array(img, np.uint8) # 입력 영상 복재
    if color == 'blue' or color == 0:  # 파란색 비율 변경
        # ([가로모든열, 세로모든열, 0=파랑] * 비율)
        dst[:, :, 0] = cv2.multiply(dst[:, :, 0], scale) 
    elif color=='green' or color==1: # 초록색 비율 변경
        # ([가로모든열, 세로모든열, 1=초록] * 비율)
        dst[:, :, 1]=cv2.multiply(dst[:,:,1], scale)
    elif color=='red' or color==2: # 빨강 비율 변경
        # ([가로모든열, 세로모든열, 2=빨] * 비율)
        dst[:, :, 2] = cv2.multiply(dst[:,:,2], scale)
    return dst  # 변경 영상 반환

# 2. 밝기 변경 함수 설정
def set_brightness(img, scale): # (영상, 밝기 변경할 값)
    return cv2.add(img, scale) #전체 픽셀값에 scale 더해 밝기변경

# 3. 대비 변경 함수 설정
def set_contrast(img, scale): # (이미지, 대비 변경할 값)
    return np.uint8(np.clip((1+scale)*img - 128*scale, 0, 255)) # 대비를 scale 비율로 변환
    # (1+scale)*img: (1 + 0.1)*이미지 픽셀값 = 대비증가
    # 128*scale: 128(256의 중간값)*0.1 = 대비조절
    # np.clip(): 0~255 넘지 않게. 넘으면 희/검이므로.
    # uint8 : OpenCV는 보통 8비트 부호 없는 정수형식으로 표현

# 4. 이미지 사이즈 변경 함수 설정
def set_size(img, scale):
    return cv2.resize(img, dsize=(int(img.shape[1]*scale), int(img.shape[0]*scale)), interpolation=cv2.INTER_AREA)

# 카메라 영상 받아올 객체 생성(영상 소스, 해상도 설정)
capt = cv2.VideoCapture(0)
capt.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
capt.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

while True:
    ret, frame = capt.read() # ret: T/F, frame: 받은 영상
    
    # 원본 이미지
    cv2.imshow("original", frame)

    # 빨간색 강조 이미지 구현
    # redFilter = color_filter(frame, 'red', 1.2)
    # cv2.imshow('Redder', redFilter)

    # 20픽셀 밝아진 이미지 구현
    # brightened = set_brightness(frame, 20)
    # cv2.imshow('Brighter', brightened)

    # 대비를 0.9로 변경한 이미지 구현
    # contra = set_contrast(frame, 0.9)
    # cv2.imshow("Contrast", contra)

    # 사이즈 2배 해상도는 안 좋아짐 구현
    # big_size = set_size(frame, 2)
    # cv2.imshow("Bigger", big_size)

    if cv2.waitKey(1) == ord('q'): # 1: 1밀리초 대기, 0: 무한
        break

capt.release()
cv2.destroyAllWindows()