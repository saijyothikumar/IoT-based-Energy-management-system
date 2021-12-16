/*
Program: Send Integers to Raspberry Pi
File: send_ints_to_raspberrypi.ino
Description: Send integers from Arduino to a Raspberry Pi
Author: Addison Sears-Collins
Website: https://automaticaddison.com
Date: July 5, 2020
*/
 
// Initialize the variables with some randomly-chosen integers
// that could represent servo motor angles, for example.
#include <SoftwareSerial.h>
SoftwareSerial mySerial(9, 10);
#include <RBDdimmer.h>//https://github.com/RobotDynOfficial/RBDDimmer

//Parameters
const int zeroCrossPin  = 2;
const int acdPin  = 3;
dimmerLamp acd(acdPin);
int trigPin = 11;    // Trigger
int echoPin = 12;    // Echo
int motor = 13;
long duration, cm;
int tank_l=100;
float percent;
int light_pin=5;
int fan_pin=6;
int glow;
char msg;
int switch11, switch12, temp1, intensity1, message, bill, main_sw;
int currentPin = A2; // Current sensor output
int voltPin = A1;
const int averageValue = 500;
long int currentValue = 0;  // variable to store the sensor value read
long int voltValue = 0;
float cur_voltage = 0;
float current = 0;
float current_five;
float voltage;
float power;
float R1 = 2000.0;
float R2 = 1000.0;
void setup(){
   
  // Set the baud rate  
  mySerial.begin(9600);   // Setting the baud rate of GSM Module  
  Serial.begin(9600);    // Setting the baud rate of Serial Monitor (Arduino)
  pinMode(light_pin, OUTPUT);
  pinMode(fan_pin, OUTPUT);
  //Define inputs and outputs
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
  acd.begin(NORMAL_MODE, ON);
}

void SendMessage(int bill)
{
  char text_to_send[30];
  mySerial.println("AT+CMGF=1");    //Sets the GSM Module in Text Mode
  delay(1000);  // Delay of 1000 milli seconds or 1 second
 
  mySerial.println("AT+CMGS=\"+917893952083\"\r");
  delay(1000);
 sprintf(text_to_send, " yor electricity bill is: %d", bill);
  mySerial.println(text_to_send);// The SMS text you want to send
  delay(100);
 
 
   mySerial.println((char)26);// ASCII code of CTRL+Z
   Serial.println("message sent");
  delay(1000);
 
}
 
void loop(){
  digitalWrite(trigPin, LOW);
  delayMicroseconds(10);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(20);
  digitalWrite(trigPin, LOW);
 
 
  pinMode(echoPin, INPUT);
  duration = pulseIn(echoPin, HIGH);
 
 
  cm = (duration/2) / 29.1;     // Divide by 29.1 or multiply by 0.0343
  if(cm>100){
    cm=30;
    }
  //inches = (duration/2) / 74;   // Divide by 74 or multiply by 0.0135
  percent =((tank_l-cm)*100)/tank_l;
  if (percent < 70){
  digitalWrite(motor, HIGH);
  }
  else if(percent>90){
    digitalWrite(motor, LOW);
  }
  if(Serial.available() > 0) {
    switch11 = Serial.parseInt();
    switch12 = Serial.parseInt();
    temp1 = Serial.parseInt();
    intensity1 = Serial.parseInt();
    main_sw = Serial.parseInt();
    message = Serial.parseInt();
    bill = Serial.parseInt();
    //glow=(intensity1*2.55);
    if(switch11==0 && switch12== 0 && temp1==0  && intensity1== 0 && main_sw==0  && message== 0 && bill==0){
    }
    else{
      for (int i = 0; i < averageValue; i++)
        {
          currentValue += analogRead(currentPin);
          voltValue += analogRead(voltPin);
        }
      
        currentValue = currentValue / averageValue;
        voltValue = voltValue / averageValue;
        cur_voltage = currentValue * 5.0 / 1024.0;
        voltage = ((voltValue *5.0*((R1 + R2)/R2))/1024);
        current_five = (cur_voltage - 2.45) / 0.185;
        power=current_five*voltage;
      Serial.print(switch11); Serial.print(",");
      Serial.print(switch12); Serial.print(",");
      Serial.print(temp1); Serial.print(",");
      Serial.print(intensity1); Serial.print(",");
      Serial.print(message); Serial.print(",");
      Serial.print(power); Serial.print(",");
      Serial.print(percent); Serial.print(",");
      Serial.println(main_sw);
      if (main_sw==1){
        if(switch11==1){
          acd.setPower(intensity1);  
          }
         else if(switch11==0){
          acd.setPower(0);  
          }
          if(switch12==1){
          analogWrite(fan_pin,250);  
          }
         else if(switch12==0){
          analogWrite(fan_pin,0);  
          }
        }
     if (message==1){
      SendMessage(bill);
      }
}}}
