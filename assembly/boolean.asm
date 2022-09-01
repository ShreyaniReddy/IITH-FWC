.include "/root/shreyani/assignment/IITH-FWC/assembly/m328Pdef.inc"
.def Y = r23
.def U = r19
.def V = r20
.def W = r21
.def mask = r22
.def result = r24
.def temp = r25
.def temp1 = r28
;declare the output and input pins in Arduino
ldi r16, 0x00
out DDRD, r16
;the next line is for declaring the mask
ldi mask, 0x01
ldi r16, 0x20
out DDRB, r16

start:
;start the logical operations
IN r17, PIND
;store first bit in U
lsr r17
LSR r17
MOV U, r17
AND U, mask
; similarly store the bit in first position in U
lsr r17
mov V, r17
and V, mask
;this is for W
lsr r17
mov W, r17
and W, mask

mov temp, U
eor temp,mask
mov temp1, V
eor temp1,mask
and temp,temp1
mov result, temp

mov temp, V
mov temp1,W
eor temp1, mask
and temp,temp1
or result, temp


;when more number of shifts are to be done, use loops
lsl result
lsl result
lsl result
lsl result
lsl result
out PORTB, result

rjmp start
