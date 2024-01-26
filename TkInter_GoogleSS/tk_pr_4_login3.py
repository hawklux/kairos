# Daum 로그인 해보기 (Chrome Webdriver 필요)
from tkinter import *
from selenium import webdriver  #pip install selenium
from selenium.webdriver.common.by import By
import time

# ChromeOptions 객체 생성
chrome_options = webdriver.ChromeOptions()

# 같은 폴더 아니면 절대경로
chrome_path = "C:/Users/AI06/Documents/_Pr_1/Python/py_spreadsheet/chromedriver-win64"

# WebDriver 생성 시에 options 매개변수로 ChromeOptions 객체 전달
driver = webdriver.Chrome(options=chrome_options)

# Daum 로그인 페이지
url = "https://accounts.kakao.com/login/?continue=https%3A%2F%2Flogins.daum.net%2Faccounts%2Fksso.do%3Frescue%3Dtrue%26url%3Dhttps%253A%252F%252Fwww.daum.net#login"
driver.get(url)
driver.implicitly_wait(3) # 연결 시간을 주고 기다림. 그 전이라도 연결되면 넘어감.

xpath1 = "//input[@name='loginId']"
xpath2 = "//input[@name='password']"
xpath3 = "//button[@class='btn_g highlight submit']"
driver.implicitly_wait(3) 

# 글자 입력
driver.find_element(By.XPATH, xpath1).send_keys("aaaa")
driver.implicitly_wait(3) 
driver.find_element(By.XPATH, xpath2).send_keys("0000")
driver.implicitly_wait(3) 
driver.find_element(By.XPATH, xpath3).click()
driver.implicitly_wait(3) 
# 브라우저 열린 상태 유지
# 주: 이 명령을 맨 마지막에 진행하지 않으면 이후 코드도 진행이 안 됨.
input("Press Enter to close.")  # 터미널 입력 받을 때까지 대기.

# 브라우저 종료
driver.quit()