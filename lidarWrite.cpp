#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <unistd.h>
#include <time.h>
#include <iostream>
#include <fstream>
using namespace std;

int main()
{
    ofstream myfile;
    ofstream myfile1;
    myfile1.open("lidar_point.txt");
    srand(time(NULL));
    int x,y,z;

    int i = 0;
    int j = 0;
    for(i;i<5000;i++){
          myfile.open("data.txt");

          x = rand()%1000;
          y = rand()%1000;
          z = rand()%1000;
          myfile << x <<" "<< y <<" "<< z << endl;
 	  myfile1 << x <<" "<< y <<" "<< z << endl;
          myfile.close();
          usleep(30000);
    }


  return 0;
}
