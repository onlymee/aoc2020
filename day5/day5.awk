function bcd(s) {
	dec=0
	for (i=1; i<=length(s);i++) {
		dec=2*dec + strtonum(substr(s,i,1))
	}
	return dec
}

BEGIN {max=0}
{ gsub(/[BR]/,"1"); gsub(/[FL]/,"0"); v=bcd($0) ; if (v>max) max=v }
END {print max}
