#include <XBee.h>
#include <SoftwareSerial.h>

int lm35Pin = A0;
int ledPin = 7;
int ledState = 0;

XBee xbee = XBee();
SoftwareSerial xss(2, 3); // RX, TX

Rx16Response rx16 = Rx16Response();

String sicaklikS;
uint8_t payload[sizeof(int) * 5];
Tx16Request tx = Tx16Request(0x0000, payload, sizeof(payload));

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  xss.begin( 9600 );
  xbee.setSerial(xss);
  pinMode(ledPin, OUTPUT);
  digitalWrite(ledPin, LOW);
}

void loop() {
  String data;
  String success = "sccs";
  if (xss.available()){
    data = getDataXBee();

    if(data == "31") {
      float sicaklikVolt = analogRead(lm35Pin);
      sicaklikS =  String((sicaklikVolt/1023)*500);
      sicaklikS.toCharArray(payload, sizeof(uint8_t) * 5);
      Serial.println(sicaklikS);
      xbee.send(tx);
    }
    else if(data == "32") {
      ledState = 1 - ledState;
      if(ledState == 0) 
        digitalWrite(ledPin, LOW);
      else
        digitalWrite(ledPin, HIGH);
      success.toCharArray(payload, sizeof(uint8_t) * 4);
      xbee.send(tx);
    }
  }
}

String getDataXBee() {
  int veri;
  String recived = "";
  int i, topByte = 0;
  int adress[] = {0, 0};
    veri = xss.read();
    Serial.println(veri, HEX);
    if(veri == 126) { //first byte '7E'
      for(i = 0; i < 2; i++) {  // 2 times for Length
        veri = xss.read();
        Serial.println(veri, HEX);
        topByte += veri;
      }

      Serial.print("uzunluk : ");
      Serial.println(topByte);

      veri = xss.read();   // for frame type

      Serial.print("Frame Type : ");
      Serial.println(veri, HEX);

      for(i = 0; i < 2; i++) {  // 2 times for 16bit adress
        veri = xss.read();
        adress[i] = veri;
      }
      Serial.println("Adres : ");
      for(i = 0; i < 2; i++) {
        Serial.println(adress[i], HEX);
      }
      
      veri = xss.read();  // for RSSI (Signal strength)
      Serial.print("RSSI : ");
      Serial.println(veri, HEX);
      
      veri = xss.read();  // for Options
      Serial.print("Option : ");
      Serial.println(veri, HEX);

      Serial.println("Data : ");
      for(i = 0; i < (topByte - 5); i++) {
        veri = xss.read();
        Serial.println(veri, HEX);
        recived.concat(String(veri, HEX));
      }

      veri = xss.read();  // for checksum
      Serial.print("checksum : ");
      Serial.println(veri, HEX);
      
      Serial.print("#");
      Serial.println(recived);
    }

    if(topByte < 5) 
      recived = "";
      
    return recived;
}
