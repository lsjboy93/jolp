#include <Wire.h>
#include "DHT.h"
#define DHTTYPE DHT11 
byte slave_temper = 4;
int DHTPin = 7;  // 온습도센서를 오렌지보드 3번핀에 연결
byte arr[2];
DHT dht(DHTPin, DHTTYPE);
byte t = 0;
byte h = 0;
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  Wire.begin(slave_temper);
  Wire.onRequest(requestHandler);  
}
void loop() {
  t = dht.readTemperature();
  h = dht.readHumidity();
}
void requestHandler()
{  arr[0] = t;
  arr[1] = h;
  Serial.print("온도 : ");
  Serial.println(t);
  Serial.print("습도 : ");
  Serial.println(h);
  Wire.write(arr, 2);
}
