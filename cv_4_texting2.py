# 화면에 글자 출력 (예: CCTV 시간 표시)
# 준비물: fonts 폴더 만들어서 폰트 파일 넣어두기

import cv2
import datetime
from PIL import ImageFont, ImageDraw, Image #pip install pillow
import numpy as np

# VideoCapture 객체 생성
capt = cv2.VideoCapture(0)  # 0번 카메라
capt.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
capt.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# 폰트 불러옴
font = ImageFont.truetype("fonts/SCDream6.otf", 20)

# 실행
while True:
    ret, frame = capt.read()

    # 현재시각 -> 문자열로 저장
    t_now = datetime.datetime.now()
    t_now_show = t_now.strftime('%Y/%m/%d %H:%M:%S')

    # 글자가 잘 보이게 배경넣기
    cv2.rectangle(img=frame, pt1=(10,15), pt2=(350,35), color=(0,0,0), thickness=-1)
    # img: 대상 이미지, pt1, pt2: 사각형 시작/끝, (b,g,r), 굵기 -1: 채우기

    # 영상 이미지에 요소(글자) 넣기
    frame = Image.fromarray(frame) # Numpy배열 이미지 -> Pillow 배열 이미지. Pillow 기능 사용 위함.
    draw = ImageDraw.Draw(frame) # 이미지 추가 가능한 Draw 객체 생성
    draw.text(xy=(10, 15), text="지켜보고 있다! "+t_now_show, font=font, fill=(255,255,255))
    # xy: 시작 커서 위치, fill: 글자색    
    frame = np.array(frame) # 다시 Numpy 배열 이미지로 전환

    cv2.imshow("CCTV", frame)
    if cv2.waitKey(1) == ord('q'):
        break

capt.release
cv2.destroyAllWindows()
