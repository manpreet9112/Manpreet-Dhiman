#include<iostream>   //.h is not used in c++
using namespace std;
int main()
{
int accno,choice,c,damt,wamt,bal, cur_bal;
cout<<"enter your account number and current balance\n";
cin>>accno>>bal;
cout<<"press 1 for deposit\n";
cout<<"press 2 for withdraw";
cin>>c;
switch(c)
{
case 1:
 cout<<"enter amount  that you want to deposit\n";
 cin>>damt;
 cur_bal=bal+damt;
cout<<" your current balance after deposit is="<< cur_bal;
 break;

case 2:
 cout<<"enter amount that you want to withdraw\n";
 cin>>wamt;
 cur_bal=bal-wamt;
 cout<<" Balance after deduction is ="<< wamt<<"\n";
 break;
cout<<"\n";
}
}
