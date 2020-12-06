REM This is BBC Basic that runs with the BBC BASIC for SDL 2.0 interpreter - https://www.bbcbasic.co.uk/
DIM qcount%(25)
rowcount%=0
answer1%=0
answer2%=0
REM Open input file
fnum=OPENIN "input.txt"
IF fnum=0 THEN PRINT "input.txt not found": END
REM Loop over lines in the file
WHILE NOT EOF# (fnum)
  line$=GET$#fnum
  IF line$="" THEN
    PROC_tallyup
  ELSE
    PROC_countqs
  ENDIF
ENDWHILE
PROC_tallyup
PRINT answer1%, answer2%
CLOSE#fnum
END
REM Procedures
DEF PROC_tallyup
FOR i = 0 TO 25
  IF qcount%(i)<>0 THEN answer1%=answer1%+1
  IF qcount%(i)==rowcount% THEN answer2%=answer2%+1
NEXT
qcount%()=0
rowcount%=0
ENDPROC
DEF PROC_countqs
rowcount%=rowcount%+1
FOR i = 1 TO LEN(line$)
  c=ASC(MID$(line$,i,1))-ASC("a")
  IF c>=0 AND c<=25 THEN qcount%(c)=qcount%(c)+1
NEXT
ENDPROC

