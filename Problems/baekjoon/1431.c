#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int compare(const void* a, const void* b)
{
	char* s1 = (char*)a;
	char* s2 = (char*)b;
	int len1 = strlen(s1), len2 = strlen(s2);
	int sum1 = 0, sum2 = 0;
	
	if (len1 != len2) {
		return len1 - len2;
	} else {
		for (int i = 0; i < len1; i++) {
			if (s1[i] < 65) sum1 += (s1[i] - '0');
			if (s2[i] < 65) sum2 += (s2[i] - '0');
		}
		if (sum1 != sum2) return sum1 - sum2;
		for (int i = 0; i < len1; i++) {
			if (s1[i] != s2[i])
				return s1[i] - s2[i];
		}
	}
}

int main()
{
	int N;
	char serial[1000][51];
	
	scanf("%d", &N);
	for (int i = 0; i < N; i++)
		scanf("%s", serial[i]);

	qsort(serial, N, sizeof(serial[0]), compare);
	
	for (int i = 0; i < N; i++)
		printf("%s\n", serial[i]);

	return 0;
}
