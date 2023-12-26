int led = 8;
int button = 2;

void setup() {
  Serial.begin(9600);
  pinMode(led, OUTPUT);
  pinMode(button, INPUT_PULLUP);
  attachInterrupt(INT0, aaa, RISING);
}

void loop() {
  digitalWrite(led, !digitalRead(led));
  delay(500);
}

void aaa(){
  Serial.println("Pressed");
}
