#include <Servo.h>

const int SERVO_TILT_PORT = 9;
const int SERVO_ROT_PORT = 10;
Servo servoRot;
Servo servoTilt;
int posRot = 0;
int posTilt = 0;

void setup() {
  Serial.begin(9600);
  pinMode(A0, INPUT);
  servoRot.attach(SERVO_ROT_PORT);
  servoTilt.attach(SERVO_TILT_PORT);
}

void loop() {
  Serial.println("running");
//  Serial.println(analogRead(A0));
//  Serial.println(analogRead(A0) / 5);
//  servo.write(analogRead(A0) / 5);
//  delay(20);

  for (posRot = 45; posRot <= 135; posRot += 9) { // goes from 0 degrees to 180 degrees
    Serial.println("Rotation");
    Serial.println(posRot);
    servoRot.write(posRot);
    delay(150);  
    for (posTilt = 45; posTilt <= 135; posTilt += 9) { // goes from 180 degrees to 0 degrees
      Serial.println(posTilt);
      servoTilt.write(posTilt);              // tell servo to go to position in variable 'pos'
      delay(50);                       // waits 15ms for the servo to reach the position
  }             
  }

}
