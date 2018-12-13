#include <XBee.h>
#include <SoftwareSerial.h>

#define lm35Pin A0
XBee xbee = XBee();
SoftwareSerial xss(2, 3); // RX, TX
String sicaklikS;
uint8_t payload[sizeof(char) * 5];
Tx16Request tx = Tx16Request(0x0000, payload, sizeof(payload));

void setup() {
  // put your setup code here, to run once:
  xss.begin( 9600 );
  xbee.setSerial(xss);
}

void loop() {
  // put your main code here, to run repeatedly:
  float sicaklikVolt = analogRead(lm35Pin);
  sicaklikS =  String((sicaklikVolt/1023)*500);
  sicaklikS.toCharArray(payload, sizeof(sicaklikS));

  xbee.send(tx);
  
  delay(5000);

}
