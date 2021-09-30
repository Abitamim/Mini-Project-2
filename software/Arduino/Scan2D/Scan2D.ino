#include <Servo.h>

const int SERVO_ROT_PORT = 10;
Servo servoRot;
int posRot = 0;
uint16_t start = 0;
int rotAmt = 15;
int rotDelta = 1;
int centerRot = 94;
float distance;
boolean ran;

void setup() {
  Serial.begin(9600);
  pinMode(A1, INPUT);
  servoRot.attach(SERVO_ROT_PORT);
  ran = false;
}

void loop() {
servoRot.write(centerRot);
delay(1000);
if (Serial.available() > 0 && !ran){
    ran = true;
  } else {
    return;
  }

servoRot.write(centerRot - rotAmt);
delay(1000);

  for (posRot = centerRot - rotAmt; posRot <= centerRot + rotAmt; posRot += rotDelta) { //   used to be 0-90
    servoRot.write(posRot);
    delay(250);
    distance = 9999;
    for (int i = 0; i < 5; i++) {
        distance = min(analogRead(A1), distance);
        delay(2);
    }
    Serial.println(String(posRot - centerRot) + ' ' + String(map(distance, 0, 1023, 0, 500)));
    delay(5); 
  }
}
