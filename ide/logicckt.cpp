#include <Arduino.h>
#include <Wire.h>
int A,U,V,W;

// the setup function runs once when you press reset or power the board
void setup() {
    pinMode(2, OUTPUT);
    pinMode(6, INPUT);
    pinMode(7, INPUT);
    pinMode(8, INPUT);
    pinMode(13,OUTPUT);

}

// the loop function runs over and over again forever
void loop() {

U = digitalRead(6);//LSB
V = digitalRead(7);
W = digitalRead(8);

A = (!U||V)&&(!V||!W);
if (A==0){
  digitalWrite(13,LOW);
}
else{
digitalWrite(13,HIGH);
}
}
