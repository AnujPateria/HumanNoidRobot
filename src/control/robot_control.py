#include <Servo.h>

Servo eyeLX, eyeLY, eyeRX, eyeRY;
Servo jaw;
Servo neckX, neckY;
Servo shoulderL, shoulderR;

bool isTalking = false;

// current positions
int eyeX = 90, eyeY = 90;
int neckXpos = 90, neckYpos = 90;
int jawPos = 40;
unsigned long lastMove = 0;

void setup() {
  Serial.begin(115200);

  eyeLX.attach(2); eyeLY.attach(3);
  eyeRX.attach(4); eyeRY.attach(5);
  jaw.attach(6);
  neckX.attach(7); neckY.attach(8);
  shoulderL.attach(9); shoulderR.attach(10);

  setNeutral();
}

void setNeutral() {
  eyeLX.write(eyeX); eyeRX.write(eyeX);
  eyeLY.write(eyeY); eyeRY.write(eyeY);
  jaw.write(jawPos);
  neckX.write(neckXpos);
  neckY.write(neckYpos);
  shoulderL.write(90);
  shoulderR.write(90);
}

void loop() {
  handleSerial();
  autoEyesNeck();
  talkingJaw();
}

// ---------------------------------

void handleSerial() {
  if (Serial.available()) {
    char c = Serial.read();

    if (c == 'T') { // Talking
      int v = Serial.parseInt();
      isTalking = (v == 1);
    }

    if (c == 'S') { // Shoulders
      int l = Serial.parseInt();
      int r = Serial.parseInt();
      shoulderL.write(l);
      shoulderR.write(r);
    }
  }
}

// ---------------------------------

void autoEyesNeck() {
  if (millis() - lastMove > 300) {  // smooth movement
    lastMove = millis();

    eyeX += random(-4,5);
    eyeY += random(-4,5);
    neckXpos += random(-3,4);
    neckYpos += random(-3,4);

    eyeX = constrain(eyeX, 60, 120);
    eyeY = constrain(eyeY, 60, 120);
    neckXpos = constrain(neckXpos, 60, 120);
    neckYpos = constrain(neckYpos, 60, 120);

    eyeLX.write(eyeX); eyeRX.write(eyeX);
    eyeLY.write(eyeY); eyeRY.write(eyeY);
    neckX.write(neckXpos);
    neckY.write(neckYpos);
  }
}

// ---------------------------------

void talkingJaw() {
  if (isTalking) {
    jaw.write(40 + random(0,40)); // speaking motion
  } else {
    jaw.write(40); // closed mouth
  }
}
