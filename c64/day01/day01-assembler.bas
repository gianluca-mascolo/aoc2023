rem assembler code for usr function usr(x) that return val of charcode or -1
10 for a = 5120 to 5148 : read d : poke a, d: next
20 data 32,170,177,152,201
30 data 48,144,13,201,58
40 data 176,9,233,47,168
50 data 169,0,32,145,179
60 data 96,160,255,169,255
70 data 32,145,179,96
rem install usr function with poke
80 poke 785,0:poke 786,20
rem x0 and x1 calibration digits, s calibration sum
90 dim x(2):s=0
100 open 1,8,2,"example,s"
110 input#1,a$
120 x(0)=-1:x(1)=-1:l=len(a$)
130 for i=1 to l
rem read from front of string
140 if x(0)=-1 then x(0)=usr(asc(mid$(a$,i,1)))
rem read from back of string
150 if x(1)=-1 then x(1)=usr(asc(mid$(a$,l+1-i,1)))
rem if both digits set then break
160 if x(0)>=0 and x(1)>=0 then i=l
170 next i
180 s=s+x(0)*10+x(1)
190 if st=0 then 110
200 close 1
210 print "calibration:"s
