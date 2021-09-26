#include <Servo.h>

const int SERVO_TILT_PORT = 9;
const int SERVO_ROT_PORT = 10;
Servo servoRot;
Servo servoTilt;
int posRot = 0;
int posTilt = 0;
int p[] = {-25.285041938862830,80.424586008651660};
uint16_t start = 0;

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
  if (Serial.available() > 0){
    start = Serial.read();
//    Serial.println(start);
  } else {
    return;
  }
  for (posRot = 22; posRot <= 76; posRot += 9) { //   used to be 0-90
//    Serial.println("Rotation");
    servoRot.write(posRot);
    delay(1000);  
    for (posTilt = 90; posTilt <= 125; posTilt += 5) { // goes from 180 degrees to 0 degrees
          servoTilt.write(posTilt); 
          delay(1000);     
         // tell servo to go to position in variable 'pos'
          Serial.println(map(analogRead(A0), 0, 1023, 0, 500));
  
    }             
  }

}
