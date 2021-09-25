#include <Servo.h>

const int SERVO_TILT_PORT = 9;
const int SERVO_ROT_PORT = 10;
Servo servoRot;
Servo servoTilt;
int posRot = 0;
int posTilt = 0;
int p[] = {8.264070477002113,-5.180794628332823};


void setup() {
  Serial.begin(9600);
  pinMode(A0, INPUT);
  servoRot.attach(SERVO_ROT_PORT);
  servoTilt.attach(SERVO_TILT_PORT);
}

void loop() {
  Serial.println(analogRead(A0));
//  Serial.println(analogRead(A0) / 5);
//  servo.write(analogRead(A0) / 5);
//  delay(20);

  for (posRot = 45; posRot <= 135; posRot += 9) { // goes from 0 degrees to 180 degrees
////    Serial.println("Rotation");

    servoRot.write(posRot);
    delay(150);  
    for (posTilt = 45; posTilt <= 135; posTilt += 9) { // goes from 180 degrees to 0 degrees
           servoTilt.write(posTilt); 
                 delay(50);     
          Serial.println(posRot);
      Serial.println(posTilt);
                 // tell servo to go to position in variable 'pos'
          Serial.println(analogRead(A0));
                    // waits 15ms for the servo to reach the position
  }             
  }

}
