#include <MsTimer2.h>
#define led 8
#define button 2

void setup() {
  Serial.begin(9600);
  pinMode(led, OUTPUT);
  pinMode(button, INPUT_PULLUP); //아두이노 자체 풀업
  MsTimer2::set(10,aa); //10msec마다 aa 실행
  MsTimer2::start();
}

void loop() {
  digitalWrite(led, HIGH);
  delay(500);
  digitalWrite(led, LOW);
  delay(500);
}

void aa(){
  if(digitalRead(button)==0){ //풀업이니 누르면 LOW
    Serial.println("Pressed");
    digitalWrite(led, LOW);
  }
}
