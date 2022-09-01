#include <avr/io.h>
#include <util/delay.h>

int main (void)
{
  unsigned char u, v, w, y, in;
#define mask 0x01
  DDRD = 0x00;
  DDRB = 0x20;
while(1){
  in = PIND;
  in = in>>2;
  u = in& mask;
  in = in>>1;
  v = in& mask;
  in = in>>1;
  w = in& mask;
  y = (!u&&!v) || (v&&!w);

  if (y == 1) {
    PORTB = ((1 <<  PB5));
  }
  else {PORTB = ((0 << PB5));}
}
}
