#include <Servo.h>

const int SERVO_PORT = 14;
Servo servo;
int pos = 0;

void setup() {
  Serial.begin(9600);
  pinMode(A0, INPUT);
  servo.attach(SERVO_PORT);
}

void loop() {
//  Serial.println(analogRead(A0));
//  Serial.println(analogRead(A0) / 5);
//  servo.write(analogRead(A0) / 5);
//  delay(20);

  for (pos = 0; pos <= 180; pos += 1) { // goes from 0 degrees to 180 degrees
    // in steps of 1 degree
    servo.write(pos);              // tell servo to go to position in variable 'pos'
    delay(15);                       // waits 15ms for the servo to reach the position
  }
  for (pos = 180; pos >= 0; pos -= 1) { // goes from 180 degrees to 0 degrees
    servo.write(pos);              // tell servo to go to position in variable 'pos'
    delay(15);                       // waits 15ms for the servo to reach the position
  }
}
