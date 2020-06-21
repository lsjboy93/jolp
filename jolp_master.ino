#include <Wire.h>
#include <SoftwareSerial.h>
int bluetoothTx = 2;
int bluetoothRx = 3;
byte slave_temper = 4;
byte slave_fire = 8;
byte slave_micro = 12;
byte recvDataBuf[4];
String str = "";
SoftwareSerial bluetooth(bluetoothTx, bluetoothRx);
void setup() {
 Wire.begin();
 Serial.begin(9600);
 bluetooth.begin(9600); //블루투스 통신 초기화
}
void loop() {
  reserveMSG();
  sendblue();
  delay(1000);
}
void reserveMSG() //값을 요구
{  Wire.requestFrom(slave_temper, 2);
  for(int i=0;i<2;i++)
  {
    recvDataBuf[i] = Wire.read();
    Serial.print(recvDataBuf[i]);
    Serial.print(" ");
    str.concat(recvDataBuf[i]);
    str.concat(" ");
  }
  //recvDataBuf[0] : 온도
  //recvDataBuf[1] : 습도
  Wire.requestFrom(slave_fire, 1);
  recvDataBuf[2] = Wire.read();
  Serial.print(recvDataBuf[2]);
  Serial.print(" ");  
  str.concat(recvDataBuf[2]);
  str.concat(" ");
  //recvDataBuf[2] : 화재 유무
  
  Wire.requestFrom(slave_micro, 1);
  recvDataBuf[3] = Wire.read();
  Serial.print(recvDataBuf[3]);
  Serial.print(" ");
  str.concat(recvDataBuf[3]);
 //recvDataBuf[3] : 감지 유무
  Serial.println();
  
}void sendblue()
{    //reserveMSG();
    /*
    for(int i=0;i<4;i++)
    {
        bluetooth.print(recvDataBuf[i]);
    }*/
    bluetooth.print(str);
    bluetooth.println();
    Serial.println(str);
    str.remove(0);
}