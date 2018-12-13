#include <SoftwareSerial.h>
SoftwareSerial XBee(2, 3); 
// XBee(Dout, Din)

String veri;
String sicaklikS;

void setup(){
 Serial.begin(9600);
  XBee.begin(9600);
  }

int c;
  
void loop() {
  if(Serial.available())  
  {
    c = Serial.read();
    XBee.write(c);
    Serial.write(c);
  }

  if(XBee.available())  
  {
    Serial.println( XBee.read());
  }  
}
