REM This is BBC Basic that runs with the BBC BASIC for SDL 2.0 interpreter - https://www.bbcbasic.co.uk/
LET fnum=OPENIN "input.txt"
IF fnum=0 THEN PRINT "input.txt not found": END
LET maxseat%=0
LET minseat%=1024
LET totalseat%=0
WHILE NOT EOF# (fnum)
  LET line$=GET$#fnum
  LET seat%=FN_b2d(line$)
  LET totalseat%=totalseat%+seat%
  IF seat%>maxseat% THEN maxseat%=seat%
  IF seat%<minseat% THEN minseat%=seat%
ENDWHILE
PRINT "Max seat in input:",maxseat%
PRINT "My seat:",FN_sumrange(minseat%,maxseat%)-totalseat%
CLOSE#fnum
END
DEF FN_sumrange(a,b) = (a+b)*(b-a+1)/2
DEF FN_b2d(bin$)
LET dec%=0
FOR i% = 1 TO LEN(bin$)
  LET c$ = MID$(bin$,i%,1)
  IF c$="B" OR c$="R" THEN LET dec%=2*dec%+1 ELSE LET dec%=2*dec%
NEXT
=dec%
