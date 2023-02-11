// find the longest pallindrome in the string
// This program is designed to find the longest palindrome in a given string
// ie. if the string given is 'djhfacdadcaop' the longest palindrom is 'acdadca' 
// which should be the return value for the function longest pallindrome(char* s).

#include<iostream>
using namespace std;

void printSubStr(
	string str, int low, int high)
{
	for (int i = low; i <= high; ++i)
		cout << str[i];
}

int longestPalSubstr(string str)
{
	int n = str.size();

	bool table[n][n];

	memset(table, 0, sizeof(table));

	int maxLength = 1;

	for (int i = 0; i < n; ++i)
		table[i][i] = true;

	int start = 0;
	for (int i = 0; i < n - 1; ++i) {
		if (str[i] == str[i + 1]) {
			table[i][i + 1] = true;
			start = i;
			maxLength = 2;
		}
	}

	for (int k = 3; k <= n; ++k) {
		for (int i = 0; i < n - k; ++i) {
			int j = i + k - 1;

			if (table[i + 1][j] && str[i] == str[j]) {
				table[i][j] = true;

				if (k > maxLength) {
					start = i;
					maxLength = k;
				}
			}
		}
	}

	cout << "Longest palindrome substring is: ";
	printSubStr(str, start, start + maxLength - 1);
    cout << endl << "with length: ";

	// return length of LPS
	return maxLength;
}

// Driver Code
int main()
{
	string str = "forgeeksskeegfor";
	cout << longestPalSubstr(str) << endl;
	return 0;
}

