# 영상 조정 코드 (색상, 밝기, 대비)
# 클래스 파일: 외부 파일에서 불러 쓸 수 있게 함수를 모아놓음.

import cv2
import numpy as np

class ImageProcessor:
    def __init__(self, video_source=0, width=640, height=480):
        self.capt = cv2.VideoCapture(video_source)
        self.capt.set(cv2.CAP_PROP_FRAME_WIDTH, width)
        self.capt.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

    # 1. 색상 변경 함수 설정
    def color_filter(self, img, color, scale): # 이미지, 색상, 비율
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
    def set_brightness(self, img, scale): # (영상, 밝기 변경할 값)
        return cv2.add(img, scale) #전체 픽셀값에 scale 더해 밝기변경

    # 3. 대비 변경 함수 설정
    def set_contrast(self, img, scale): # (이미지, 대비 변경할 값)
        return np.uint8(np.clip((1+scale)*img - 128*scale, 0, 255)) # 대비를 scale 비율로 변환
        # (1+scale)*img: (1 + 0.1)*이미지 픽셀값 = 대비증가
        # 128*scale: 128(256의 중간값)*0.1 = 대비조절
        # np.clip(): 0~255 넘지 않게. 넘으면 희/검이므로.
        # uint8 : OpenCV는 보통 8비트 부호 없는 정수형식으로 표현

    # 4. 이미지 사이즈 변경 함수 설정
    def set_size(self, img, scale):
        return cv2.resize(img, dsize=(int(img.shape[1]*scale), int(img.shape[0]*scale)), interpolation=cv2.INTER_AREA)

    # 카메라 영상 받아올 객체 생성(영상 소스, 해상도 설정)
    capt = cv2.VideoCapture(0)
    capt.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    capt.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    def run_editing(self):
        while True:
            ret, frame = self.capt.read() # ret: T/F, frame: 받은 영상
            
            # 원본 이미지
            cv2.imshow("original", frame)

            # 빨간색 강조 이미지 실행
            redFilter = self.color_filter(frame, 'red', 1.2)
            cv2.imshow('Redder', redFilter)

            # 20픽셀 밝아진 이미지 실행
            brightened = self.set_brightness(frame, 20)
            cv2.imshow('Brighter', brightened)

            # 대비를 0.9로 변경한 이미지 실행
            contra = self.set_contrast(frame, 0.9)
            cv2.imshow("Contrast", contra)

            # 사이즈 2배 해상도는 안 좋아짐 실행
            big_size = self.set_size(frame, 2)
            cv2.imshow("Bigger", big_size)

            if cv2.waitKey(1) == ord('q'): # 1: 1밀리초 대기, 비워두면 프레임 1장만 찍힘.
                break

        self.capt.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    # 원본 파일이 직접 실행될 때(타 파일의 새 객체 포함)만 실행됨.
    processor = ImageProcessor()  # 객체 생성
    processor.run_editing()