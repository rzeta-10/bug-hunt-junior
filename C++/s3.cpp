// find the bug in the concept

#include<iostream>
using namespace std;

int i = 5;
int j; #variable j should be initalized or else it takes the garbage value

int foo(int j) {
  for (i=0; i<j; i++){
    cout << i << " ";
  }
  return j;
}

void ineedj(void) {
  cout << "j is " << j << "\n";
}

main() {
  int j;
  j = foo(i);
  ineedj();
}
