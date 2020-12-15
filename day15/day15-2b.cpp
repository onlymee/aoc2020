
#include <iostream>
#include <array>

int *spoken;

int play(int playTo, int lastspoken, int lastturn) {
    int next=0;
    while (lastturn<playTo) {
        if (spoken[lastspoken]==0) {
            next=0;
        } else {
            next=lastturn-spoken[lastspoken];
        }
        spoken[lastspoken]=lastturn;
        lastturn++;
        lastspoken=next;
    }
    return(lastspoken);
}

int main()
{
    spoken[0]=1;
    spoken[1]=3;
    spoken[3]=4;
    spoken[7]=5;
    spoken[14]=2;
    
    std::cout << play(30000000,9,6) << '\n';
    delete [] spoken;
}