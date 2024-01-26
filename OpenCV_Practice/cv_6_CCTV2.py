# CCTV: 움직임이 있을때만 영상을 캡쳐
#

import cv2
import datetime
from PIL import ImageFont, ImageDraw, Image
import numpy as np
import os

# 프레임 비교 함수
def get_diff_img(frame_a, frame_b, frame_c, threshold):
    # 비교용 프레임 3개의 영상을 모두 흑백으로 전환
    frame_a_gray = cv2.cvtColor(frame_a, cv2.COLOR_BGR2GRAY)
    frame_b_gray = cv2.cvtColor(frame_b, cv2.COLOR_BGR2GRAY)
    frame_c_gray = cv2.cvtColor(frame_c, cv2.COLOR_BGR2GRAY)

    # 프레임 비교: 1-2, 2-3
    diff_ab = cv2.absdiff(frame_a_gray, frame_b_gray)
    diff_bc = cv2.absdiff(frame_b_gray, frame_c_gray)

    # diff가 threshold 이상이면 값을 255(백색)으로 변환함
    ret, diff_ab_t = cv2.threshold(diff_ab, threshold, 255, cv2.THRESH_BINARY)
    ret, diff_bc_t = cv2.threshold(diff_bc, threshold, 255, cv2.THRESH_BINARY)
    
    # 2에서도 변하고 3에서도 변한 부분 AND연산 > 1로 변환
    diff = cv2.bitwise_and(diff_ab_t, diff_bc_t)
    # 영상에서 morphology로 빈 공간을 적당히 채움 
    k = cv2.getStructuringElement(cv2.MORPH_CROSS, (3,3))
    diff = cv2.morphologyEx(diff, cv2.MORPH_OPEN, k)
    # 영상에서 1인 부분의 갯수를 셈
    diff_cnt = cv2.countNonZero(diff)
    return diff, diff_cnt

# 초기 설정 (영상 소스 객체 생성, 해상도 설정)
capt = cv2.VideoCapture(0)
capt.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
capt.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# 코덱, 폰트, 녹화 상태 설정
codex = cv2.VideoWriter_fourcc(*'XVID') #fourcc: 코덱 식별을 위한 4글자 코드 = XVID: MPEG-4 기반 코덱. 동영상 저장 시 필요. 화면만 캡쳐할 때는 불필요. 
font = ImageFont.truetype('fonts/SCDream6.otf', 20)
is_record = False  # 상태값: 초기에는 녹화 안 함 세팅
on_record = False

threshold = 40   # 영상차이 판별 기준값
diff_min = 10    # 영상차이 '픽셀'의 수(이 이상이면 움직였음)
cnt_record = 0   # 녹화 시간 변수
min_cnt_record = 5 # 최소 촬영시간

# 1, 2번 이미지 프레임 저장
ret, frame_a = capt.read()
ret, frame_b = capt.read()

# 실행
while True:
    # 현재 영상
    ret, frame_c = capt.read()
    frame = np.array(frame_c)

    # 현재 시각 문자열로
    t_now = datetime.datetime.now()
    t_str = t_now.strftime('%Y/%m/%d %H:%M:%S')
    t_str_path = t_now.strftime('%Y_%m_%d %H_%M_%S') #파일명으로 못쓰는 특수문자 _로 변경
    cv2.rectangle(img=frame, pt1=(10,15), pt2=(340,35), color=(0,0,0), thickness=-1) # 글자 넣을 검은 네모 배경

    # 움직임 감지
    diff, diff_cnt = get_diff_img(frame_a=frame_a, frame_b = frame_b, frame_c=frame_c, threshold = threshold)

    # 움직임이 일정 이상인가?
    if diff_cnt > diff_min:
        cv2.imwrite("Capture/captured"+t_str_path+".png", frame) # 캡쳐 이미지 담을 폴더명/파일명(Capture 폴더를 만들어둬야 함)
    
    # 영상 차이를 출력(테스트용. 실제 사용 시 꺼도 됨.)
    cv2.imshow("diff", diff)
    
    # 이미지에 글자 등 요소 넣기
    frame = Image.fromarray(frame) # Numpy배열 이미지 -> Pillow 배열 이미지. Pillow 기능 사용 위함.
    draw = ImageDraw.Draw(frame) # 이미지 추가 가능한 Draw 객체 생성
    draw.text(xy=(10,15), text="보고있다~ "+t_str, font=font, fill=(255,255,255))
    frame = np.array(frame)
    frame_a = np.array(frame_b) # 하나씩 다음 프레임으로! 
    frame_b = np.array(frame_c) 

    key = cv2.waitKey(1000) #1s 동안 키입력 대기
    if key == ord('q'):
        break
    cv2.imshow("Original", frame)

capt.release()
cv2.destroyAllWindows()

