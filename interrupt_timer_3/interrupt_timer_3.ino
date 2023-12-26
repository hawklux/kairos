#include <MsTimer2.h>
#define led 8
#define button 2
boolean tt = true;

void setup() {
  Serial.begin(9600);
  pinMode(led, OUTPUT);
  pinMode(button, INPUT_PULLUP); //아두이노 자체 풀업
  MsTimer2::set(500,aa); //10msec마다 aa 실행
  MsTimer2::start();
}

void loop() {
  if(digitalRead(button) == LOW){
    Serial.println("Pressed");
  }
}

void aa(){
  digitalWrite(led, tt);
  tt = !tt;
}
