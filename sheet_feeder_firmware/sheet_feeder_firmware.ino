/*
 * Company: Impossible Objects
 * Author: Drew Marschner
 * Date: 9/18/2020
 * 
 * Code for driving sheet feeding test fixture for use in the CBAM process.
 * 
 * TODO:
 * - Allow for 'configurations' sent from python
 * - Stop using this stupid grbl board and just use some motor shields, get rid of all of this unnecessary gcode crap
 * - Remove delays and send data once grbl is ready - cleaner/faster solution
 * - Move all the variable and function declarations to header file
 */

#include <Servo.h>

const int feed_sheet_command = '1';
const int nudger_switch_up = 0;
const int nudger_switch_down = 1;

const char nudger_axis = 'y';
const char takeaway_axis = 'z';
const char elevator_axis = 'x';

const float elevator_feed_distance = 0.043;
const float nudger_feed_distance = 0.35;
const float feeder_feed_distance = 1.75;
const float takeaway_feed_distance = 4;
const float motor_speed = 200;
const float max_raised_distance = 10.;
const bool motor_lock = false;


const int nudger_engage_pos = 134;
const int nudger_retract_pos = 163;
const int nudger_control_pin = 3;
const int nudger_switch_pin = 2;

enum nudger_direction { UP, DOWN };

String elevator_feed_command;
String nudger_feed_command;
String feeder_feed_command;
String takeaway_feed_command;
String motor_speed_command;

int nudger_switch_status;
Servo nudger;
String inLine;

void setup() {
  Serial.begin(115200);

  // Set up nudger
  pinMode(nudger_switch_pin, INPUT);
  nudger.attach(nudger_control_pin);
  nudger.write(nudger_retract_pos);
  
  // continuously try to connect to the grbl board
  while (!connect_grbl()) {
    Serial.println("Retrying in 3 seconds...");
    delay(3000);
  };
  setup_grbl();
}

bool connect_grbl() {
  Serial.print("Connecting to gShield...");
  Serial1.begin(115200);
  delay(100);
  Serial1.write("\r\n\r\n");
  delay(500);
  String in = read_grbl();
  if (in.length() > 0) {
    Serial.println("connected");
    return true;
  } else {
    Serial.println("Not connected.");
    return false;
  }
}

void setup_grbl() {
  /**
   * Set up grbl with the configuration parameters
   */
  // Define all speed and movement strings according to configuration variables
  elevator_feed_command = String(String(elevator_axis) + String(elevator_feed_distance));
  nudger_feed_command = String(String(nudger_axis) + String(nudger_feed_distance));
  feeder_feed_command = String(String(nudger_axis) + String(feeder_feed_distance) + String(takeaway_axis) + String(feeder_feed_distance));
  takeaway_feed_command = String(String(takeaway_axis) + String(takeaway_feed_distance));
  motor_speed_command = String("F" + String(motor_speed));
  
  // Check whether or not to lock the motors when not running - probably only useful for FAR
  if (motor_lock) {
    Serial1.println("$1=255");
  } else {
    Serial1.println("$1=0");
  }

  // Set feeder into relative mode
  Serial1.println("G91");
  
  // Set motor speed
  Serial1.println(motor_speed_command);
}

String read_grbl() {
  /**
   * Read output from grbl board.
   * @return string output from grbl board.
   */
  while (Serial1.available()) {
    inLine += Serial1.readString();
    delay(2);
  }
  return inLine;
}

void raise_stack() {
  /**
   * Raise the stack by a set amount, but also check if it needs further raising in order to fully engage the nudger.
   */
  delay(200);
  Serial1.println(elevator_feed_command);
  nudger_switch_status = digitalRead(nudger_switch_pin);
  float raised_distance = 0.;
  Serial.print("Nudger switch status: ");
  Serial.println(nudger_switch_status);
  while ((nudger_switch_status == nudger_switch_down) && (raised_distance < max_raised_distance)) {
    raised_distance = raised_distance + elevator_feed_distance;
    Serial1.println(elevator_feed_command);
    delay(50);
    Serial.println("Raising elevator to engage nudger...");
    nudger_switch_status = digitalRead(nudger_switch_pin);
  }

  if (nudger_switch_status == nudger_switch_down) {
    Serial.println("Error! No sheets detected by nudger!");
  }
}

void drive_nudger(nudger_direction dir) {
  /**
   * Drives nudger servo up or down.
   */
  if (dir == UP) {
    nudger.write(nudger_retract_pos);
  } else {
    nudger.write(nudger_engage_pos);
  }
}


void acquire_sheet() {
  /**
   * acquire a sheet into the retard nip, raise elevator if necessary
   */
  drive_nudger(DOWN);
  raise_stack();
  Serial1.println(nudger_feed_command);
  delay(500);
  drive_nudger(UP);
}

void feed_takeaway_sheet() {
  /**
   * Feeds sheet through
   */
  Serial1.println(feeder_feed_command);
  drive_nudger(UP);
  Serial1.println(takeaway_feed_command);
}

/// <summary>  </summary>
void move_sheet() {
  /**
   * Moves a sheet through the test fixture, records relevant data
   */
  acquire_sheet();
  feed_takeaway_sheet();
}

void sheet_feed_control() {
  /**
   * Basic control loop, waits for confirmation to move a sheet or exit.
   */
  while (!Serial.available()) {}

  int readByte = Serial.read();
  Serial.print("Received: ");
  Serial.println(readByte);
  if (readByte == feed_sheet_command) {
    Serial.println("Moving sheet");
    move_sheet();
  }
}

void loop() {
  /**
   * Arduino loop function
   */
  sheet_feed_control();
}
