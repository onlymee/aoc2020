BEGIN { RS="\n\n"; FS="\n"; answer1=0 ; answer2=0 }
{ 
    delete qcount
	for (i=1; i<=NF;i++) {
        for (j=1; j<=length($i);j++) qcount[substr($i,j,1)]++
	}
    for (letter in qcount) {
        if (qcount[letter]>0)   answer1++;
        if (qcount[letter]==NF) answer2++;
    }
}
END { print answer1, answer2 }
