#include<iostream>
#include<octave/oct.h>
#include"graphics.h"
using namespace std;
using namespace oct;
int main()
{
  Matrix  img;
  img=img.imread("/home/manpreet/Desktop/nature1.jpg");
  imshow(img);
  return 0;
}
