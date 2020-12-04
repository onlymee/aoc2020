# FPAT require gawk not awk!


BEGIN { RS="\n\n"; FPAT="[a-z]+:[#[:alnum:]]+"; valid1=0; valid2=0}
{
    delete record
    for (i=1;i<=NF; i++) {
      n=split($i,parts,":")
      if (n==2) record[parts[1]]=parts[2];
    }
      
    if( "byr" in record &&
        "iyr" in record &&
        "eyr" in record &&
        "hgt" in record &&
        "hcl" in record &&
        "ecl" in record &&
        "pid" in record) { valid1++ }

    if ( record["byr"]~/^19[2-9][0-9]|200[0-2]$/ &&
         record["iyr"]~/^201[0-9]|2020$/ &&         
         record["eyr"]~/^202[0-9]|2030$/ &&
         (record["hgt"]~/^(59|6[0-9]|7[0-6])in$/ ||
             record["hgt"]~/^(1[5-8][0-9]|19[0-3])cm$/) &&
         record["hcl"]~/^#[0-9a-f]{6}$/ &&
         record["ecl"]~/^amb|blu|brn|gry|grn|hzl|oth$/ &&
         record["pid"]~/^[0-9]{9}$/) 
    {
        valid2++; 
    }
}
END {print valid1, valid2}