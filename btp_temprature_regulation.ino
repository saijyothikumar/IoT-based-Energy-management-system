int pinTemp = A3;   //This is where our Output data goes
int temp1=0;
int fan_pin=6;
int fan_speed=0;
int rot;
void setup() {
  Serial.begin(9600);     
}
void loop() {
  float temp = analogRead(pinTemp);    //Read the analog pin
  Serial.print("voltage:");
  Serial.print(((temp*5)/1023));
  Serial.println("V");
  temp = temp*0.48;   // convert output (mv) to readable celcius
 
  Serial.print("Temperature: ");
  Serial.print(temp);
  Serial.println("C");  //print the temperature status
  if (temp1>temp){
    if (fan_speed!=0){
      Serial.print("reduce speed");
      if (temp1-temp>5){
      fan_speed=fan_speed-1;
      }}
    }
  if (temp1<temp){
    if (fan_speed!=5){
      Serial.println("increase speed");
      if (temp-temp1>5){
      fan_speed=fan_speed+1;
      }}
    }
 rot=(fan_speed*50);
 analogWrite(fan_pin, rot); 
 Serial.println(fan_speed);
  delay(5000);  
}
