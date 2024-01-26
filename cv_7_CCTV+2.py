# 움직임이 있을 때 동영상 녹화

import cv2
import datetime
from PIL import ImageFont, ImageDraw, Image
import numpy as np

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

# 카메라 영상을 받아올 객체 선언 및 설정(영상 소스, 해상도 설정)
capt = cv2.VideoCapture(0)
capt.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
capt.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# 코덱, 폰트, 녹화 상태 설정
codex = cv2.VideoWriter_fourcc(*'XVID') #fourcc: 코덱 식별을 위한 4글자 코드 = XVID: MPEG-4 기반 코덱. 동영상 저장 시 필요.
font_ = ImageFont.truetype('fonts/SCDream6.otf', 20)
is_record = False  # 녹화 전반 제어
on_record = False  # 녹화 중 이벤트 제어

threshold = 40   # 영상차이 판별 기준값
diff_min = 10    # 영상차이 '픽셀'의 수(이 이상이면 움직였음)
min_cnt_record = 5 # 최소 5초 이상 촬영(아니면 사진이 됨)
cnt_record = 0   # 녹화 시간 변수(남은 촬영시간 측정용)

# 초기 프레임(1, 2번) 저장
ret, frame_a = capt.read()
ret, frame_b = capt.read()

# 실행
while True:
    # 현재 영상
    ret, frame_c = capt.read()

    # 움직임 감지
    diff, diff_cnt = get_diff_img(frame_a=frame_a, frame_b=frame_b, frame_c=frame_c, threshold=threshold)

    # 움직임이 일정 이상이면
    if diff_cnt > diff_min:
        is_record = True     # 녹화 준비!
        if on_record == False: #녹화 중 이벤트 진행 안 함?
            #video_ 객체 생성(파일명(한글가능), 인코더, 초당 프레임 수, (가로,세로크기))로 영상 쓸 준비해
            video_ = cv2.VideoWriter("Capture/내가_다_봤다"+t_str_path+".avi", codex, 1, (frame_c.shape[1], frame_c.shape[0]))
        cnt_record = min_cnt_record
    if is_record == True:     # 녹화 준비 됐나?
        print('녹화 중')
        video_.write(frame_c)  #현재 프레임 저장
        cnt_record -= 1   # 남은 녹화시간 루프당 1초씩 차감
        on_record = True  # 녹화 중이니까 위 이벤트 준비 No
    if cnt_record == 0:   # 남은 녹화시간=0 > 촬영종료
        is_record = False
        on_record = False

    # 영상 차이를 출력(테스트용. 실제 사용 시 꺼도 됨.)
    cv2.imshow("Recording in progress", diff)
    frame = np.array(frame_c)

    # 현재 시각 문자열로
    t_now = datetime.datetime.now()
    t_str = t_now.strftime('%Y/%m/%d %H:%M:%S')
    t_str_path = t_now.strftime('%Y_%m_%d %H_%M_%S') # 파일명으로 못쓰는 특수문자 _로 대체
    cv2.rectangle(img=frame, pt1=(10,15), pt2=(340,35), color = (0,0,0), thickness=-1) #글자용 검은 네모 배경

    # 이미지에 글자 등 요소 넣기
    frame = Image.fromarray(frame)  # Numpy배열 이미지 -> Pillow 배열 이미지. Pillow 기능 사용 위함.
    draw = ImageDraw.Draw(frame) # 이미지 추가 가능한 Draw 객체 생성
    draw.text(xy=(10, 15), text="나 안 잔다 "+t_str, font=font_, fill=(255,255,255)) # xy: 시작 커서 위치, fill: 글자색

    frame = np.array(frame) # 다시 Numpy 배열 이미지로 전환
    frame_a = np.array(frame_b)
    frame_b = np.array(frame_c)

    key = cv2.waitKey(1000) # 1초 대기
    if key == ord('q'):
        break
    cv2.imshow("Original", frame) #현재 시간 있는 영상

capt.release()
cv2.destroyAllWindows()
    