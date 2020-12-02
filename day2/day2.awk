function countc(c,s) { return gsub(c,"",s) }


BEGIN { FS="[ :-]+" }
{print}
countc($3,$4) >= $1 &&
       countc($3,$4) <= $2 { valid1++ }
countc($3,substr($4,$1,1)substr($4,$2,1)) == 1 { valid2++ }
END { print valid1, valid2 }
