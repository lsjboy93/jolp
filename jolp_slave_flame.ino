#include <Wire.h>
int ledPin = 13;
int inputPin = 7;
int pirState = LOW;
int val = 0;           
int minSecsBetweenEmails = 60;
long lastSend =  -minSecsBetweenEmails * 10001;
 byte address = 100;
 byte slave_fire = 8;
 byte recvDataBuf[128];
 char str[100];
  byte senddata = 0;
 byte rsvdata = 0;
 void setup() {
  Serial.begin(9600);
  Wire.begin(address);
  Wire.begin(slave_fire);
  Wire.onRequest(requestHandler);
  // LED 를 출력으로 설정합니다.
  pinMode(ledPin, OUTPUT);      
  // 센서를 입력으로 설정합니다.
  pinMode(inputPin, INPUT);    
}
void loop(){
}
void requestHandler()
{    long now = millis();
    val = digitalRead(inputPin); 
    if (val == HIGH) {           
        digitalWrite(ledPin, HIGH); 
        pirState = LOW;
        Serial.println("Beware of fire.");
    } else {   
        digitalWrite(ledPin, LOW);     
        pirState = HIGH;
        Serial.println("FIRE!!!!");
    }
    Wire.write(pirState);
}