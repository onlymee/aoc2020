
#include <iostream>
#include <map>

int play(int playTo,std::map<int,int> spoken, int lastspoken, int lastturn) {
    int next=0;
    while (lastturn<playTo) {
        if (spoken.contains(lastspoken)) {
            next=lastturn-spoken[lastspoken];
        } else {
            next=0;
        }
        spoken.insert_or_assign(lastspoken,lastturn);
        lastturn++;
        lastspoken=next;
    }
    return(lastspoken);
}


int main()
{
    std::map<int,int> spoken;

    spoken.insert({0,1});
    spoken.insert({1,3});
    spoken.insert({3,4});
    spoken.insert({7,5});
    spoken.insert({14,2});
    
    std::cout << play(30000000,spoken,9,6) << '\n';
}