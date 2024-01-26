#include <Servo.h>

Servo servoA;
Servo servoB;
Servo servoC;
Servo servoD;

int cur_angles[4] = {0,0,0,0};
int angleA, angleB, angleC, angleD;

int extractNumber(String str, char identifier){
  int startIndex = str.indexOf(identifier) + 1;
  int endIndex = startIndex;
  while (isdigit(str[endIndex])){
    endIndex++;
  }

  // 부분 문자열을 추출하여 정수로 변환
  String numberStr = str.substring(startIndex, endIndex);
  return numberStr.toInt();
}

void setup() {
  Serial.begin(9600);
  servoA.attach(9); // servoA = pin 9
  servoB.attach(10); // servoB = pin 10
  servoC.attach(11); // servoC = pin 11
  servoD.attach(12); // servoD = pin 12
  servoA.write(0);
  servoB.write(0);
  servoC.write(0);
  servoD.write(0);
}

void loop() {
  if (Serial.available() > 0) {
    String inputString = Serial.readStringUntil('\n'); // 한 줄 끝까지 읽기
    inputString.trim(); // 앞뒤 공백 제거
    
    // 함수 호출 전에 extractNumber를 정의해야 함
    angleA = extractNumber(inputString, 'a');
    angleB = extractNumber(inputString, 'b');
    angleC = extractNumber(inputString, 'c');
    angleD = extractNumber(inputString, 'd');
    
//    if (inputString.startsWith("a")) {
//      int angleA = inputString.substring(1).toInt(); // 숫자 추출 + 정수변환
    angleA -= cur_angles[0];
    servoA.write(angleA); // servoA 이동
    cur_angles[0] = angleA;
//    } else if (inputString.startsWith("b")) {
//      int angleB = inputString.substring(1).toInt();
    angleB -= cur_angles[1];
    servoB.write(angleB);
    cur_angles[1] = angleB;
//    } else if (inputString.startsWith("c")) {
//      int angleC = inputString.substring(1).toInt();
    angleC -= cur_angles[2];
    servoC.write(angleC);
    cur_angles[2] = angleC;
//    } else if (inputString.startsWith("d")) {
//      int angleD = inputString.substring(1).toInt();
    angleD -= cur_angles[3];
    servoD.write(angleD);
    cur_angles[3] = angleD;
//    }
  }
}
