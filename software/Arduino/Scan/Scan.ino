#include <Servo.h>

//define constants
const int SERVO_TILT_PORT = 9;
const int SERVO_ROT_PORT = 10;
Servo servoRot;
Servo servoTilt;
int posRot = 0;
int posTilt = 0;
int rotAmt = 15;
int tiltAmt = 30;
int rotDelta = 1;
int tiltDelta = 1;
int centerRot = 94;
int centerTilt = 87;;

float distance;

boolean ran; //use to stop running after first run through

void setup() {
  Serial.begin(9600);
  pinMode(A1, INPUT);
  servoRot.attach(SERVO_ROT_PORT);
  servoTilt.attach(SERVO_TILT_PORT);
  ran = false;
}

void loop() {

//start directly facing test piece
servoRot.write(centerRot);
delay(1000);
servoTilt.write(centerTilt);
delay(1000);

//only run if received signal from reading script
if (Serial.available() > 0 && !ran){
    ran = true; //ensure it doesn't run again without reset
  } else {
    return;
  }

//go to initial position and give extra time to go there in case sensor was far away
servoRot.write(centerRot - rotAmt);
delay(1000);
servoTilt.write(centerTilt - tiltAmt);
delay(1000);

  for (posRot = centerRot - rotAmt; posRot <= centerRot + rotAmt; posRot += rotDelta) { 
    servoRot.write(posRot);
    delay(250);
    servoTilt.write(centerTilt - tiltAmt); //go to starting tilt angle
    delay(250);
    for (posTilt = centerTilt - tiltAmt; posTilt <= centerTilt + tiltAmt; posTilt += tiltDelta) {
          servoTilt.write(posTilt); 
          delay(10);
          distance = 9999;
          //get minimum of 5 readings
          for (int i = 0; i < 5; i++) {
            distance = min(analogRead(A1), distance);
            delay(2);
          }
          //send data to python script
          Serial.println(String(posTilt - centerTilt) + ' ' + String(posRot - centerRot) + ' ' + String(map(distance, 0, 1023, 0, 500)));
          delay(5);
    }   
    Serial.println();          
  }
}
