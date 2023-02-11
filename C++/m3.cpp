// find the bug in the concept used in the code -- no fix

#include<iostream>
using namespace std;

char *initialize() {
  char string[80];
//   string = "hello"
  char* ptr = string;
  return ptr;
}

void do_something_with(char* myval){
	cout << "the variable initialized is " << *myval << endl;
}

main() {
	cout << "enter value for myval" << endl;
  char *myval = initialize();
  cin >> *myval;
  cout << "Variable intialized" << endl;
  do_something_with(myval);
}
