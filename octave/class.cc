#include<iostream>
using namespace std;
//#include "conio.h"
class top                       //base class
{
public :
int a;
void getdata()
{
cout<<"\n\nEnter first Number :::\t";
cin>>a;
}
void putdata()
{
cout<<"\nFirst Number Is :::\t"<<a;
}
};

//First level inheritance
class middle :public top      // class middle is derived_1 
{
public:
int b;
void square()
{
getdata();
b=a*a;
cout<<"\n\nSquare Is :::"<<b;
}
};

//Second level inheritance 
class bottom :public middle    // class bottom is derived_2 
{
public:
int c;
void cube()
{
square();
c=b*a;
cout<<"\n\nCube :::\t"<<c;
}
};

int main()
{
//clrscr();
bottom b1;
b1.getdata();
b1.cube();
b1.putdata();
return 0;
}
