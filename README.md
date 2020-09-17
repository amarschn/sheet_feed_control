# sheet_feed_control
Control for sheet feeding fixture

Copy-paste of some sample arduino code for reference for altering control methodology:

########################################
String inLine;

void setup() {
  Serial.begin(115200);
  Serial1.begin(115200);
  delay(100);
  Serial1.write("\r\n\r\n");
  delay(1000);
  Serial1.write("G91");
  delay(500);
}

void loop() {
  // put your main code here, to run repeatedly:
  while (Serial1.available()) {
    inLine += Serial1.readString();
    delay(2);
  }
  Serial.println(inLine);
  inLine = "";
  delay(200);
  Serial1.println("G1X0.5");
  delay(1000);
  Serial1.println("G1X-0.5");
  delay(1000);
}

##############################

#include <Servo.h>

Servo myservo;
#define ENGAGE_POS 134
#define RETRACT_POS 163
#define SERVO_PIN 3
#define SERVO_CONTROL_PIN 4
#define SWITCH_PIN 2

int read_signal;
int pin_status = 0;

void setup() {
  // put your setup code here, to run once:
  pinMode(SWITCH_PIN, INPUT);

  pinMode(SERVO_CONTROL_PIN, INPUT);
  myservo.attach(SERVO_PIN);  // attaches the servo on pin 2 to the servo object
  myservo.write(RETRACT_POS);
  Serial.begin(115200);
}

void loop() {
  // put your main code here, to run repeatedly:
  delay(100);
  pin_status = digitalRead(SWITCH_PIN);
  Serial.println(pin_status);
  delay(100);

  read_signal = digitalRead(SERVO_CONTROL_PIN);
  if (read_signal == 0) {
    myservo.write(RETRACT_POS);
  }
  else if (read_signal == 1) {
    myservo.write(ENGAGE_POS);
  }
}
