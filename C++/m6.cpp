// the below code doesn't work for some values of s. find the bug

#include<iostream>
#include<string>

int main(){
    std :: string s = "Hello World";

    for(int i=0;i < s.length(); i++){
        s[i] = toupper(s[i]);
    }

    std::cout << s << std::endl;

    return 1;
}
