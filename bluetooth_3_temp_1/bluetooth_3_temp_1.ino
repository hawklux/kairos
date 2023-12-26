#include <DHT.h>
#include <SoftwareSerial.h>

DHT myDHT (A0, DHT11);        //객체화
SoftwareSerial myBlueT (2,3); // Tx, Rx 설정

void setup() {
  myBlueT.begin(9600); // 블루투스 9600으로 가동
  myDHT.begin();       // 센서 가동
}

void loop() {
  float temper = myDHT.readTemperature();
  myBlueT.println("t"+String(temper)); //'t'붙여 전송
  delay(1000);
  float humid = myDHT.readHumidity();
  myBlueT.println("h"+String(humid)); //'h'붙여 전송
  delay(1000); 
}
