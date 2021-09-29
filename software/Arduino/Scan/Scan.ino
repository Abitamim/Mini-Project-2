#include <Servo.h>

const int SERVO_TILT_PORT = 9;
const int SERVO_ROT_PORT = 10;
Servo servoRot;
Servo servoTilt;
int posRot = 0;
int posTilt = 0;
int p[] = {-25.285041938862830,80.424586008651660};
uint16_t start = 0;
int rotAmt = 30;
int tiltAmt = 30;
int rotDelta = 1;
int tiltDelta = 1;
int centerRot = 94;
int centerTilt = 82;
float distance;

void setup() {
  Serial.begin(9600);
  pinMode(A0, INPUT);
  servoRot.attach(SERVO_ROT_PORT);
  servoTilt.attach(SERVO_TILT_PORT);
}

void loop() {
  
//  Serial.println(analogRead(A0) / 5);
//  servo.write(analogRead(A0) / 5);
//  delay(20);
//    servoRot.write(0);
//    delay(1000);
//    servoRot.write(90);
//    delay(1000);
//    servoTilt.write(90);
//    delay(1000);    
//    servoTilt.write(135);
//    delay(1000);
//    Serial.println(map(analogRead(A0), 0, 1023, 0, 500));
//  Serial.println("reading");
//  if (Serial.available() > 0){
//    start = Serial.read();
////    Serial.println(start);
//  } else {
//    return;
//  }

servoRot.write(centerRot - rotAmt);
delay(1000);
servoTilt.write(centerTilt - tiltAmt);
delay(1000);


  for (posRot = centerRot - rotAmt; posRot <= centerRot + rotAmt; posRot += rotDelta) { //   used to be 0-90
//    Serial.println("Rotation");
    servoRot.write(posRot);
    delay(250);
    servoTilt.write(centerTilt - tiltAmt);
    delay(250);
    for (posTilt = centerTilt - tiltAmt; posTilt <= centerTilt + tiltAmt; posTilt += tiltDelta) { // goes from 180 degrees to 0 degrees
          servoTilt.write(posTilt); 
          delay(10);
          distance = 9999;
          for (int i = 0; i < 5; i++) {
            distance = min(analogRead(A0), distance);
            delay(2);
          }
          Serial.println(map(distance, 0, 1023, 0, 500));
          delay(5);
    }   
    Serial.println();          
  }
//  Serial.println("next set");
//  Serial.println(map(analogRead(A0), 0, 1023, 0, 500));
}
