#include <iostream>
#include <fstream>
#include <vector>
using namespace std;


long toboggan (const vector<string> hillMap, int dx, int dy)
{
  int trees=0, x=dx, y=dy;
  int height = hillMap.size();
  int width = hillMap[0].length();

  while(y<height)
  {
  //  cout << " x=" << x << " y= " << y << " " << hillMap[y][x % width] << endl;
    if (hillMap[y][x % width]=='#') trees++;
    x+=dx;
    y+=dy;
  }

  return trees;
}

int main() 
{
    ifstream inputFile;
    vector<string> hillMap;

    inputFile.open("input.txt", ios::in);
    while (!inputFile.eof()) 
    {
      string line;
      getline(inputFile,line);
      hillMap.push_back(line);
    }

    long trees = toboggan(hillMap,3,1);
    cout << "Part 1: Trees = " << trees << endl;

    trees = trees * toboggan(hillMap,1,1)
                  * toboggan(hillMap,5,1)
                  * toboggan(hillMap,7,1)
                  * toboggan(hillMap,1,2);
    cout << "Part 2: Tree Product = " << trees << endl;

    return 0;
}

