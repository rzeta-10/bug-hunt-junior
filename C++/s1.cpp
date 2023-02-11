// to find the reverse of a given number

#include<iostream>
using namespace std;

int reverse(int x) {
    long r=0;                                  
    while(x){
        r=r*10+x%10;
        x=x/10;                                   
    }
    return r;
}

int main(void){
    cout << reverse(12345) << endl;
}
