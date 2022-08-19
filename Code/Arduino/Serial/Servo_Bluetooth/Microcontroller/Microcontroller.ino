# include <SoftwareSerial.h>
# include <Servo.h>

# define RX A0
# define TX A1
# define finger1 5
# define finger2 6
# define finger3 9
# define finger4 10
# define finger5 11

Servo servo1;
Servo servo2;
Servo servo3;
Servo servo4;
Servo servo5;

String input = "11111";
Servo servo[5] = {servo1, servo2, servo3, servo4, servo5};  

SoftwareSerial Bluetooth(RX, TX);

void finger_open(int i) {
  servo[i].write(0);
  Serial.print(i+1);
  Serial.println(": opened");
}

void finger_close(int i) {
  servo[i].write(150);
  Serial.print(i+1);
  Serial.println(": closed");
}

void setup() {
  Serial.begin(9600);
  Bluetooth.begin(9600);

  pinMode(TX, OUTPUT);
  pinMode(RX, INPUT);
  pinMode(finger1, INPUT);
  pinMode(finger2, INPUT);
  pinMode(finger3, INPUT);
  pinMode(finger4, INPUT);
  pinMode(finger5, INPUT);

  servo1.attach(finger1);
  servo2.attach(finger2);
  servo3.attach(finger3);
  servo4.attach(finger4);
  servo5.attach(finger5);

  for (int i = 0; i < 5; i++){
    finger_close(i);
  }

  delay(1500);
  
  for (int i = 0; i < 5; i++){
    finger_open(i);
  }
  Serial.println("Begin");
}

void loop() {
  if (Bluetooth.available() > 0) {
    Serial.println("Bluetooth available");
    input = Bluetooth.readStringUntil('\n');
    for (int i = 0; i < 5; i++){
      if (input[i] == '0') {
        finger_close(i);
      }
      else if (input[i] == '1') {
        finger_open(i);
      }
    }
    Serial.println("");
  }
}
