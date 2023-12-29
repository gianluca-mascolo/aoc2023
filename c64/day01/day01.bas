10 f=0
20 s=0
30 open 1,8,2,"example,s"
40 get#1,a$
50 d=val(a$)
60 c=asc(a$)
70 if c=13 then 150
80 if f=0 and c>=48 and c<=57 then 110
90 if f=1 and c>=48 and c<=57 then l=d
100 goto 170
110 f=1
120 s=s+d*10
130 l=d
140 goto 170
150 f=0
160 s=s+l
170 if st=0 then 40
180 close 1
190 print "calibration:"s


