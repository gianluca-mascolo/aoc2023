.a 1400  20 aa b1 jsr $b1aa ; FACINX Convert number in FAC to 16-bit signed integer (Y=LB, A=HB)
.a 1403  98       tya       ; Trasfer register Y in accumulator. We need only 1 byte because PETSCII charmap range is from 0 to 255
.a 1404  c9 30    cmp #$30  ; PETSCII $30 is "0"
.a 1406  90 0d    bcc $1415 ; Branch if A < #$30
.a 1408  c9 3a    cmp #$3a  ; PETSCII char before $3a is $39 or "9"
.a 140a  b0 09    bcs $1415 ; Branch if A >= $3a
.a 140c  e9 2f    sbc #$2f  ; Subtract $2f
.a 140e  a8       tay       ; Transfer accumulator in register Y
.a 140f  a9 00    lda #$00  ; High byte is always zero
.a 1411  20 91 b3 jsr $b391 ; Convert 16-bit signed integer to floating point number in FAC. (Y=LB, A=HB)
.a 1414  60       rts
.a 1415  a0 ff    ldy #$ff  ; ffff is -1
.a 1417  a9 ff    lda #$ff
.a 1419  20 91 b3 jsr $b391
.a 141c  60       rts
