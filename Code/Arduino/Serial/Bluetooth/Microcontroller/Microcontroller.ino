# include <SoftwareSerial.h>
# define LED 7
# define RX 3
# define TX 2
String input;  

SoftwareSerial Bluetooth(RX, TX);

void setup() {
  Serial.begin(9600);
  Bluetooth.begin(9600);
  pinMode(LED, OUTPUT);
  pinMode(TX, OUTPUT);
  pinMode(RX, INPUT);

}

void loop() {
  if (Bluetooth.available() > 0) {
    input = Bluetooth.readStringUntil('\n');
    if (input == "on") {
      digitalWrite(LED, HIGH);
      Bluetooth.write("LED on");
      Serial.println("LED on");
    }
    else if (input == "off") {
      digitalWrite(LED, LOW);
      Bluetooth.write("LED off");
      Serial.println("LED off");
    }
    else{
      Bluetooth.write("Invald input");
    }
  }
}
