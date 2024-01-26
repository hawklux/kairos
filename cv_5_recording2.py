# 영상 녹화, 영상 화면 캡쳐

import cv2
import datetime
from PIL import ImageFont, ImageDraw, Image
import numpy as np

# 카메라 객체 생성(영상 소스, 해상도 설정)
capt = cv2.VideoCapture(0)
capt.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
capt.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

codex = cv2.VideoWriter_fourcc(*"XVID") #fourcc: 코덱 식별을 위한 4글자 코드 = XVID: MPEG-4 기반 코덱
font_ = ImageFont.truetype('fonts/SCDream6.otf', 20)
is_record = False   # 상태값: 초기에는 녹화 안 함 세팅

# 실행
while True:
    ret, frame = capt.read()

    # 현재시간 문자열로 저장
    t_now = datetime.datetime.now()
    t_str = t_now.strftime('%Y/%m/%d %H:%M:%S')
    t_str_path = t_now.strftime('%Y_%m_%d %H_%M_%S') # 파일명으로 못쓰는 특수문자를 _로 대체함

    cv2.rectangle(img=frame, pt1=(10,15), pt2=(340,35), color=(0,0,0), thickness=-1)

    # 영상에 글자 등 요소 넣기
    frame = Image.fromarray(frame) # Numpy배열 이미지 -> Pillow 배열 이미지. Pillow 기능 사용 위함.
    draw = ImageDraw.Draw(frame) # 이미지 추가 가능한 Draw 객체 생성
    draw.text(xy=(10,15), text="보고 있다! "+t_str, font=font_, fill=(255,255,255)) # xy: 시작 커서 위치, fill: 글자색
    frame = np.array(frame) # 다시 Numpy 배열 이미지로 전환

    key = cv2.waitKey(30)
    if key == ord('r') and is_record == False:
        is_record = True    # 상태값: 녹화 중
        #video_ 객체 생성(파일명(한글가능), 인코더, 초당 프레임 수, 영상크기)로 영상 쓸 준비
        video_ = cv2.VideoWriter("본 결과다"+t_str_path + ".avi", codex, 15, (frame.shape[1], frame.shape[0]))
    elif key == ord('r') and is_record == True:
        is_record = False   # 상태값: 녹화 중지
        video_.release      # 녹화 종료
    elif key == ord('c'):
        # 화면 1장 캡쳐: (파일명 영어만, 이미지)
        cv2.imwrite("recorded "+t_str_path+".png", frame)
    elif key == ord('q'):  # 무한루프 중단
        break

    if is_record == True:   # 상태값: 녹화 중이면
        # video_ 객체에 현재 프레임 저장
        video_.write(frame)
        # 빨간점으로 녹화 중 표시
        cv2.circle(img=frame, center=(620, 15), radius=5, color=(0,0,255), thickness=-1)
    cv2.imshow("Recording in progress", frame)

capt.release()
cv2.destroyAllWindows()
