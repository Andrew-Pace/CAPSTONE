#include <ESP32Servo.h>
#include <Arduino.h>
#include <Wire.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>

#define CLK 10
#define DT 20
#define SW 21
#define SERVO 0
#define MOTOR 4
#define BUTTON1 1
#define BUTTON2 2
#define SWITCH 3

#define SCREEN_WIDTH 128 // OLED display width, in pixels
#define SCREEN_HEIGHT 64 // OLED display height, in pixels

float servo_sensitivity = 1; // 
float motor_sensitivity = 1;

int motor_usec = 1000; 
int servo_usec = 1500;
int currentStateCLK;
int lastStateCLK;
int pulseCount = 0; // Variable to count pulses
bool pitch_selected = true;
bool button_pressed = false;
bool in_menu = false;
int switchbutton_counter = 0;
int button_hold_counter = 0;
bool manual_control_mode_active = true;
bool button1_pressed = false;
bool button2_pressed = false;
bool servo_sent = false;
bool motor_sent = false;

int num_of_menu_items = 1; // 1 means 2

Servo pitch_servo;
Servo motor_fauxservo;
Adafruit_SSD1306 display(SCREEN_WIDTH, SCREEN_HEIGHT, &Wire, -1);

void UpdateDisplay(){
//Update The Display With all the info
  if (servo_usec == pitch_servo.readMicroseconds()) {servo_sent = true;} else {servo_sent = false;}
  if (motor_usec == motor_fauxservo.readMicroseconds()) {motor_sent = true;} else {motor_sent = false;}
  // Update the display
  display.clearDisplay();
  if (in_menu) {
    display.setCursor(0, 0); display.print("MENU:");
    display.setCursor(0, 20); display.print("SerSens: "); display.print(servo_sensitivity); if(switchbutton_counter == 0){display.print("   <--");}
    display.setCursor(0, 30); display.print("MotSens: "); display.print(motor_sensitivity); if(switchbutton_counter == 1){display.print("   <--");}
  } else {
    if (manual_control_mode_active){display.setCursor(0, 0); display.print("MANUAL CONTROL ACTIVE");
      display.setCursor(0, 9); display.print("USE CAUTION");}
    display.setCursor(0, 20); display.print("Servo: "); display.print(servo_usec); if (pitch_selected) { display.print("   <--"); }
    display.setCursor(0, 30); display.print("Servo Reading: "); display.print(pitch_servo.readMicroseconds());
    display.setCursor(0, 40); display.print("Motor: "); display.print(motor_usec); if (pitch_selected == false) { display.print("   <--"); }
    display.setCursor(0, 50); display.print("Motor Reading: "); display.print(motor_fauxservo.readMicroseconds());
  }
  display.display();
}

void CheckButtons(){
  // CHECKBUTTONS
  // CHECK BUTTON1
  if (digitalRead(BUTTON1) == LOW && button1_pressed == false){ //First Detection of Button1
    button1_pressed = true;
    if (pitch_selected){pitch_servo.writeMicroseconds(servo_usec);}
    if (!pitch_selected){motor_fauxservo.writeMicroseconds(motor_usec);}

    UpdateDisplay();
    delay(50);
  }
  if (digitalRead(BUTTON1) == HIGH){
    button1_pressed = false;
    
  }

  // CHECK BUTTON2
  if (digitalRead(BUTTON2) == LOW && button2_pressed == false){ //First Detection of Button2
    button2_pressed = true;
  }
  if (digitalRead(BUTTON2)== HIGH && button2_pressed == true){// First detection of release
    button2_pressed = false;
  }

  // CHECK KNOBBUTTON
  if (digitalRead(SW) == LOW) {
    if (button_pressed == false){ // if button is detected for the first time
      Serial.println("Button pressed!");
      button_pressed = true;
    }
    if (button_pressed == true) { // If button was already detected in a previous loop
      button_hold_counter++;
    }
    UpdateDisplay();
    Serial.println(button_hold_counter);
  }
  if (digitalRead(SW) == HIGH){ // when button is not detected
    if (button_pressed == true){ // if last loop button was pressed
      button_pressed = false;
      if (button_hold_counter <= 50){
        if (in_menu){
          switchbutton_counter ++;
          if (switchbutton_counter > num_of_menu_items){switchbutton_counter = 0;}
        }
        if (!in_menu){pitch_selected = !pitch_selected;}
      }
      if (button_hold_counter > 50){
        in_menu = !in_menu; // Toggle menu mode
      }
    button_hold_counter = 0;
    UpdateDisplay();
    }
  }

  // CHECK SWITCH
  if (digitalRead(SWITCH) == LOW){
    if (manual_control_mode_active == false){
      manual_control_mode_active = true;
      UpdateDisplay();
    }
    
  }
  else {
    if (manual_control_mode_active == true){
      manual_control_mode_active = false;
      UpdateDisplay();
    }
  }

}

void setup() {
  pinMode(CLK, INPUT);
  pinMode(DT, INPUT);
  pinMode(SW, INPUT_PULLUP); // Use internal pull-up resistor for the switch
  pinMode(BUTTON1, INPUT_PULLUP);pinMode(BUTTON2, INPUT_PULLUP);pinMode(SWITCH, INPUT_PULLUP);

  Serial.begin(115200); // Start serial communication at 115200 baud
  pitch_servo.attach(SERVO, 500, 2500);
  motor_fauxservo.attach(MOTOR, 1000, 2000);
  if(!display.begin(SSD1306_SWITCHCAPVCC, 0x3C)) { // Initialize with the I2C address
    Serial.println(F("SSD1306 allocation failed"));
    for(;;); // Don't proceed, loop forever
  }

  

  display.clearDisplay();
  display.setTextSize(1); // Normal 1:1 pixel scale
  display.setTextColor(SSD1306_WHITE); // Draw white text
  UpdateDisplay();
  lastStateCLK = digitalRead(CLK); // Read the initial state of CLK
}

void loop() {
  currentStateCLK = digitalRead(CLK); // Read the current state of CLK

  // If the state of CLK has changed, then we have a pulse
  if (currentStateCLK != lastStateCLK) {
    // If the DT state is different than the CLK state, then the encoder is rotating counterclockwise
    if (digitalRead(DT) != currentStateCLK) { pulseCount--; } else { pulseCount++; }

    // Only update the servo_angle after two pulses
    if (abs(pulseCount) >= 2) {
      if (in_menu) {
        if (pulseCount > 0) {
          if (switchbutton_counter == 0){servo_sensitivity += 0.1;}
          if (switchbutton_counter == 1){motor_sensitivity += 0.1;}
        } else {
          if (switchbutton_counter == 0){servo_sensitivity -= 0.1;}
          if (switchbutton_counter == 1){motor_sensitivity -= 0.1;}
        }
        servo_sensitivity = constrain(servo_sensitivity, 0.1, 10.0); // Constrain sensitivity to a reasonable range
        motor_sensitivity = constrain(motor_sensitivity, 0.1, 10.0); // Constrain sensitivity to a reasonable range
        pulseCount = 0; // Reset pulse count after updating the sensitivity
        UpdateDisplay();
      } else {
        if (pitch_selected) {
          if (pulseCount > 0) {
            servo_usec += (20 * servo_sensitivity);
          } else {
            servo_usec -= (20 * servo_sensitivity);
          }
          pulseCount = 0; // Reset pulse count after updating the servo_angle
          servo_usec = constrain(servo_usec, 500, 2500);
        }
        if (pitch_selected == false) {
          if (pulseCount > 0) {
            motor_usec += (20 * motor_sensitivity);
          } else {
            motor_usec -= (20 * motor_sensitivity);
          }
          pulseCount = 0; // Reset pulse count after updating the servo_angle
          motor_usec = constrain(motor_usec, 1000, 2000);
        }
        UpdateDisplay();
        Serial.print(servo_usec); Serial.print(motor_usec); Serial.print(button_hold_counter); Serial.println();
      }
    }
  }

  CheckButtons();

  if (manual_control_mode_active){pitch_servo.writeMicroseconds(servo_usec);motor_fauxservo.writeMicroseconds(motor_usec);}
  

  lastStateCLK = currentStateCLK; // Update lastStateCLK with the current state
}