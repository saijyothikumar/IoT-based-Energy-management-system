int trigPin = 11;    // Trigger
int echoPin = 12;    // Echo
int motor = 13;
long duration, cm, inches;
int tank_l=100;
float percent;

void setup() {
  //Serial Port begin
  Serial.begin (9600);
  //Define inputs and outputs
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
}
 
void loop() {
 
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
  /*if(percent>100){
    percent=70;
    }*/
  //Serial.print(inches);
  //Serial.print("in, ");
  //percent=40;
  Serial.print(cm);
  Serial.print("cm, ");
  Serial.print(percent);
  Serial.print(" % full");
  Serial.println();
  if (percent < 70){
  digitalWrite(motor, HIGH);
  }
  else if(percent>90){
    digitalWrite(motor, LOW);
  }
  
  
  delay(1000);

  
}
