#include <Wire.h>
byte rcwl = 7;
byte slave_micro = 12;
byte data =0;
int val =0; 
void setup() {
 Serial.begin(9600);
 pinMode(rcwl, INPUT);
 Wire.begin(slave_micro);
 Wire.onRequest(requestHandler);
}
void loop() {
  val = digitalRead(rcwl);
  delay(1000);
}void requestHandler()
{  Serial.println(val);
  Wire.write(val);
}
