# 음원: https://pixabay.com/ko/sound-effects/search/beep/
# QR코드 생성: https://me-qr.com/ 이 경우 웹스크레이핑 필요
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
            qr_link = obj.data.decode('utf-8')
            
            # 웹 스크래이핑으로 QR 코드 가져오기
            response = requests.get(qr_link)
            soup = BeautifulSoup(response.text, 'html.parser')
            kairos = soup.find('div', {'class': 'container-fluid p-4'}).text
            print("QR Code: ", kairos)

            # 사운드 효과
            playsound("sound/beep1.mp3")

        cv2.imshow("QR Cam", frame)

        key = cv2.waitKey(1)
        if key == 27:  # Esc
            break

capt.release()
cv2.destroyAllWindows()