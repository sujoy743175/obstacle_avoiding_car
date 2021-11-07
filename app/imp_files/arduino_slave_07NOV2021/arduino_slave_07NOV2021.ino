// Include NewPing Library for HC-SR04 sensor
#include <NewPing.h>
#include <Wire.h>
// Hook up 4 HC-SR04 sensors in 1-pin mode
// Sensor 0
#define TRIGGER_PIN_0  8
#define ECHO_PIN_0     8

// Sensor 1
#define TRIGGER_PIN_1  9
#define ECHO_PIN_1     9

// Sensor 2
#define TRIGGER_PIN_2  10
#define ECHO_PIN_2     10

// Sensor 3
#define TRIGGER_PIN_3  11
#define ECHO_PIN_3     11

#define leftLimitPin  12
#define rightLimitPin 4

// Maximum Distance is 260 cm
#define MAX_DISTANCE 260

// Create objects for ultrasonic sensors
NewPing sensor0(TRIGGER_PIN_0, ECHO_PIN_0, MAX_DISTANCE);
NewPing sensor1(TRIGGER_PIN_1, ECHO_PIN_1, MAX_DISTANCE);
NewPing sensor2(TRIGGER_PIN_2, ECHO_PIN_2, MAX_DISTANCE);
NewPing sensor3(TRIGGER_PIN_3, ECHO_PIN_3, MAX_DISTANCE);

// Define return data array, one element per sensor
int distance[8];

// Define counter to count bytes in response
int bcount = 0;

// interrupt

float leftTic = 0;
float rightTic = 0;
//byte leftSpeed ;
//byte rightSpeed ;
int leftOldtime = 0;
int rightOldtime = 0;
int leftTime ;
int rightTime ;
byte leftDistance;
byte rightDistance;
const byte interruptPinLeft = 2;
const byte interruptPinRight = 3;

void setup() {
  Wire.begin(8);                /* join i2c bus with address 8 */
  Wire.onReceive(receiveEvent); /* register receive event */
  Wire.onRequest(requestEvent); /* register request event */
  Serial.begin(9600);          /* start serial for debug */
  pinMode(interruptPinLeft, INPUT_PULLUP);
  pinMode(interruptPinRight, INPUT_PULLUP);
  attachInterrupt(digitalPinToInterrupt(interruptPinLeft), leftIsr, RISING);
  attachInterrupt(digitalPinToInterrupt(interruptPinRight), rightIsr, RISING);

  pinMode(leftLimitPin, INPUT_PULLUP);
  pinMode(rightLimitPin, INPUT_PULLUP);
}

void loop() {
  RightSpeed();
  LeftSpeed();
  readDistance();
}

// function that executes whenever data is received from master
void receiveEvent(int howMany) {
  while (0 < Wire.available()) {
    byte mcu = Wire.read();      /* receive byte as a character */
    Serial.print(mcu);           /* print the character */
  }
  Serial.println();             /* to newline */
}

void requestEvent() {

  // Define a byte to hold data
  byte val;

  // Cycle through data
  // First response is always 255 to mark beginning
  switch (bcount) {
    case 0:
      val = 255;
      break;
    case 1:
      val = distance[0];
      break;
    case 2:
      val = distance[1];
      break;
    case 3:
      val = distance[2];
      break;
    case 4:
      val = distance[3];
      break;
    case 5:
      val = distance[4];
      break;
    case 6:
      val = distance[5];
      break;
    case 7:
      val = distance[6];
      break;
    case 8:
      val = distance[7];
      break;
  }

  // Send response back to Master
  Wire.write(val);

  // Increment byte counter
  bcount = bcount + 1;
  if (bcount > 8) bcount = 0;

}

void readDistance()
{
  distance[0] = sensor0.ping_cm();
  if (distance[0] > 254 ) {
    distance[0] = 254;
  }
  delay(20);

  distance[1] = sensor1.ping_cm();
  if (distance[1] > 254 ) {
    distance[1] = 254;
  }
  delay(20);

  distance[2] = sensor2.ping_cm();
  if (distance[2] > 254 ) {
    distance[2] = 254;
  }
  delay(20);

  distance[3] = sensor3.ping_cm();
  if (distance[3] > 254 ) {
    distance[3] = 254;
  }
  delay(20);

  distance[4] = digitalRead(leftLimitPin);
  delay(20);

  distance[5] = digitalRead(rightLimitPin);
  delay(20);

  distance[6] = leftDistance;
  distance[7] = rightDistance;
  delay(20);
/*Serial.print("Distance...............");
Serial.println(distance[0]);
Serial.print("Distance...............");
Serial.println(distance[1]);
Serial.print("Distance...............");
Serial.println(distance[2]);*/

}


void leftIsr() {
  leftTic++;
}

void rightIsr() {
  rightTic++;
}

void LeftSpeed() {
  detachInterrupt(digitalPinToInterrupt(interruptPinLeft));
  leftTime = millis() - leftOldtime;
  leftDistance = leftTic * (21.4 / 28); // circumference of wheel = 21.4 cm and no of tic on left is 28
  //int leftSpeed = (leftDistance / (leftTime * 60000));   // /min
  leftOldtime = millis();
  Serial.println(leftDistance); // WITHOUT PRINTING THIS ERRORS FOUND IN ESP32 REPL
  Serial.println(rightDistance); // WITHOUT PRINTING THIS ERRORS FOUND IN ESP32 REPL
    Serial.println(" cm/min");
  leftTic = 0;


  attachInterrupt(digitalPinToInterrupt (interruptPinLeft), leftIsr, RISING);
  return leftDistance;
}

void RightSpeed() {
  detachInterrupt(digitalPinToInterrupt(interruptPinRight));
  rightTime = millis() - rightOldtime;
  rightDistance = rightTic * (21.4 / 28); // circumference of wheel = 21.4 cm and no of tic on left is 28
  //int rightSpeed =  (rightDistance/rightTime)  ;//rightDistance / (rightTime * 60000));   // /min
  rightOldtime = millis();
  /*Serial.print(rightSpeed);
    Serial.println(" cm/min");*/
  rightTic = 0;


  attachInterrupt(digitalPinToInterrupt (interruptPinRight), rightIsr, RISING);
  return rightDistance;

}
