
#include <XBee.h>

#include <SoftwareSerial.h>

XBee xbee = XBee();
SoftwareSerial xss(2, 3); // RX, TX
uint8_t payload[] = { 5 };
Tx16Request tx = Tx16Request(0x0000, payload, sizeof(payload));
int  pingPong = 1;

void setup()  {
  pinMode(13, OUTPUT);  
   Serial.begin(9600);
   Serial.println( "Arduino started sending bytes via XBee" );

   // set the data rate for the SoftwareSerial port
   xss.begin( 9600 );
   xbee.setSerial(xss);
}

void loop()  {
  xbee.send(tx);
  if ( pingPong == 0 )
    digitalWrite(13, LOW);
  else
    digitalWrite(13, HIGH);
  pingPong = 1 - pingPong;
  delay( 1000 );
}
