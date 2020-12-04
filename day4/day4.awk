BEGIN { RS="\n\n"; valid1=0 ; valid2=0 }
{gsub(/\n/," ")}

 /byr:/ && /iyr:/ && /eyr:/ && /hgt:/ && /hcl:/ && /ecl:/ && /pid:/ {valid1++}

 /byr:(19[2-9][0-9]|200[0-2])(\s|$)/ && 
 /iyr:(201[0-9]|2020)(\s|$)/ && 
 /eyr:(202[0-9]|2030)(\s|$)/ && 
(/hgt:(59|6[0-9]|7[0-6])in(\s|$)/ ||
 /hgt:(1[5-8][0-9]|19[0-3])cm(\s|$)/) && 
 /hcl:#[0-9a-f]{6}(\s|$)/ && 
 /ecl:(amb|blu|brn|gry|grn|hzl|oth)(\s|$)/ && 
 /pid:[0-9]{9}(\s|$)/       { valid2++ }


END { print valid1, valid2 }
