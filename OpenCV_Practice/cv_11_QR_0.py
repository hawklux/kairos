# https://www.youtube.com/watch?v=CUNVIfmfGuE 
# 음원: https://pixabay.com/ko/sound-effects/search/beep/
# 바코드/QR코드 리더기
'''
pip install opencv-python
pip install playsound==1.2.2  # Beep 사운드 재생
pip install pyzbar      # QR / Bar 코드 인식
* pyzbar 오류나면: https://www.microsoft.com/ko-KR/download/details.aspx?id=40784 다운받아 설치
pip uninstall pyzbar -> pip install pyzbar
pip install requests
pip install beautifulsoup4
'''

import cv2
import pyzbar.pyzbar as pyzbar
from playsound import playsound
import requests
from bs4 import BeautifulSoup

capt = cv2.VideoCapture(0)

while True:
    ret, frame = capt.read()

    if ret:
        for obj in pyzbar.decode(frame):
            qr = obj.data.decode('utf-8')
            print("QR Code: ", qr)
            
            # 사운드 효과
            playsound("sound/beep1.mp3")

        cv2.imshow("QR Cam", frame)

        key = cv2.waitKey(1)
        if key == 27:  # Esc
            break

capt.release()
cv2.destroyAllWindows()