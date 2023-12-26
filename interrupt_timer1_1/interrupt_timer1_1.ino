#include <TimerOne.h>

const int led = 8;
int button = 10;

void setup() {
  Serial.begin(9600);
  pinMode(led, OUTPUT);
  pinMode(button, INPUT_PULLUP);
  
  Timer1.initialize(1000); // 0.1초마다
  Timer1.attachInterrupt(aaa);
  Timer1.start();
}

void loop() {
  digitalWrite(led, !digitalRead(led));
  delay(1000);
}

void aaa(){
  if(digitalRead(button) == LOW){
    Serial.println("Pressed");
  }
}
