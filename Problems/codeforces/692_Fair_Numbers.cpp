#include <stdio.h>

int isFairNumber(long long int n) {
	long long int temp = n;
	int check[11] = {0, };

	while (temp > 0) {
		check[temp % 10] = 1;
		temp /= 10;
	}

	for (int i = 1; i < 10; i++)
		if (check[i] == 1 && n % i > 0)
			return -1;
	return 1;
}

int main() {
	int T;
	long long int n;
	
	scanf("%d", &T);
	for (int t = 0; t < T; t++) {
		scanf("%lli", &n);
		
		while (isFairNumber(n) != 1)
			n++;
		printf("%lli\n", n);
	}

	return 0;
}
