// C++ program for coin change problem
// Given an integer array of coins[ ] of size N representing
// different types of currency and an integer sum, 
// The task is to find the number of ways to make sum by using different combinations from coins[].  

#include<iostream>

using namespace std;

int count(int coins[], int n, int sum)
{
	int i, j, x, y;
	int table[sum + 1][n];								// int table[sum ][n];

	for (i = 0; i < n; i++)
		table[0][i] = 1;							// table[sum-1][i] = 1;

	for (i = 1; i < sum + 1; i++) {
		for (j = 0; j < n; j++) {

			x = (i - coins[j] >= 0) ? table[j][i - coins[j]] : 1;


			y = (j > 1) ? table[j - 1][i] : 1;


			table[i][j] = x + y;
		}
	}	
	return table[sum-1][n - 1];							
}

// Driver Code
int main()
{
	int coins[] = { 1, 2, 3 };
	int n = sizeof(coins) / sizeof(coins[0]);
	int sum = 6;
	cout << count(coins, n, sum);
	return 0;
}

