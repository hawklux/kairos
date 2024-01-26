# 아두이노 짝꿍 파일: 
import gspread
from google.auth import exceptions
from google.auth.transport.requests import Request
from google.oauth2 import service_account

teamID = 'C401_01'
sheetName = 'team1'
d_cnt = [0]

# 1. 시트 설정
# 1.1 코드 템플릿
scope = ['https://spreadsheets.google.com/feeds']
creds = None

try:
    creds = service_account.Credentials.from_service_account_file('key.json', scopes = scope)
except exceptions.MissingFileError:
    print("No key.json found.")

client = gspread.authorize(creds)

# 1.2 시트 URL 입력
doc = client.open_by_url('https://docs.google.com/spreadsheets/d/16UTQ1rmvCJx3ECAiHTEh-mk4McE6WKuE0IWzywbuMDU/edit#gid=0')

# 1.3 시트 객체 생성(시트명 입력)
mySheet = doc.worksheet(sheetName)
cell_init = ['']*12
# a1,b2,c3,d4,e5,f6,g7,h8,i9,j10,k11,l12,m13,n14

# 2. G-Sheet 실행 작업 기능
# 2.1 행 삽입 : 초기화
def newRow():
    d_cnt[0] += 1
    mySheet.insert_row(['0' for x in range(12)], 4) # 4행에 삽입
    pk = f'{teamID}_{d_cnt[0]}'
    mySheet.update_cell(4, 1, pk)

# 2.2 셀값 읽어오기 (추후 셀번호 변경)
def from_G_cell(x, y):
    value = mySheet.cell(x, y).value  # Not Null 
    cnt = str(value) if value is not None else 0
    return value

# 2.3 셀값 변경 (추후 셀 값 변경)
def to_G_cell(x, y, v):
    mySheet.update_cell(x, y, v)

## 테스트 실행
# newRow()
# newRow()
# to_G_cell(4,3,"D2024/01/20 13:01:23")

# 3. 작업 실행
# 3.1 to 아두이노
import serial
import threading
import time

portNum = "COM5"
ser = serial.Serial(portNum, 9600, timeout=1)

def to_ardu(d_out):
    ser.write((d_out+"\n").encode('utf-8'))
    ser.reset_output_buffer()

thread_in = threading.Thread(target=to_ardu, args=("dummy",), daemon=True)  # to_ardu에 인자가 없으면 args 삭제.
thread_in.start()

# 3.2 밸런싱 로봇1 성공 시 초록 LED 점등. (4,4)를 계속 모니터링 해야 함.

while True:
    bal1_v = from_G_cell(4,4)
    print(bal1_v)
    if bal1_v:
        for _ in range(10):
            to_ardu("pass\n")
            break
    else:
        to_ardu("fail\n")
        time.sleep(1)

