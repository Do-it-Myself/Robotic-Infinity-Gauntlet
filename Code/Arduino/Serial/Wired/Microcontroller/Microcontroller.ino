# define LED 7
String input;  

void setup() {
  Serial.begin(9600);
  pinMode(LED, OUTPUT);
}
void loop() {
  if (Serial.available() > 0) {
    input = Serial.readStringUntil('\n');
    if (input == "on") {
      digitalWrite(LED, HIGH);
      Serial.write("LED on");
    }
    else if (input == "off") {
      digitalWrite(LED, LOW);
      Serial.write("LED off");
    }
    else{
      Serial.write("Invald input");
    }
  }
}
