const int ledP = 13;
const int buttonP = 2;

int led_state = LOW;
bool led_state_changed = false;

void buttonOn(){
  led_state = (led_state == LOW)? HIGH:LOW;
  led_state_changed = true;
}

void setup()
{
  pinMode(ledP, OUTPUT);
  pinMode(buttonP, INPUT);
  attachInterrupt(digitalPinToInterrupt(buttonP), buttonOn, RISING);
}

void loop()
{
  if(led_state_changed){
    led_state_changed = false;
    digitalWrite(ledP, led_state);
  }
}
