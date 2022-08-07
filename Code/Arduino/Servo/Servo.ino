# include <Servo.h>

# define finger1 11
# define finger2 10
# define finger3 9
# define finger4 6
# define finger5 5

Servo servo1;
Servo servo2;
Servo servo3;
Servo servo4;
Servo servo5;

Servo servo[5] = {servo1, servo2, servo3, servo4, servo5}; 

void setup() {
  Serial.begin(9600);

  pinMode(finger1, OUTPUT);
  pinMode(finger2, OUTPUT);
  pinMode(finger3, OUTPUT);
  pinMode(finger4, OUTPUT);
  pinMode(finger5, OUTPUT);

  servo1.attach(finger1);
  servo2.attach(finger2);
  servo3.attach(finger3);
  servo4.attach(finger4);
  servo5.attach(finger5);
}

void loop () {
  servo1.write(140);
  delay(500);
  servo2.write(165);
  delay(500);
  servo1.write(0);
  delay(1000);
  servo2.write(0);
  delay(1000);
}

/* void loop () {
  servo1.write(140);
  servo2.write(165);
  servo3.write(165);
  servo4.write(165);
  servo5.write(165);
  delay(1000);
  servo1.write(0);
  servo2.write(0);
  servo3.write(0);
  servo4.write(0);
  servo5.write(0);
  delay(3000);
}
*/
