#include <stdio.h>

int N, K;
int a[1000001];
int cnt[1000001];
long long int sum[1000001];

void something(int jump, int cnt){
	int i = 0;
	while (i < N){
		a[i] += cnt;
		i += jump;
	}
}

int main(){
	int X, Q, L, R;

	scanf("%d %d", &N, &K);
	for (int i = 0; i < K; i++){
		scanf("%d", &X);
		cnt[X]++;
	}

	for (int X = 1; X <= N; X++){
		if (cnt[X] > 0)
			something(X, cnt[X]);
	}

	sum[0] = a[0];
	for (int i = 1; i < N; i++){
		sum[i] = sum[i - 1] + a[i];
	}

	scanf("%d", &Q);
	for (int i = 0; i < Q; i++){
		scanf("%d %d", &L, &R);
		if (L == 0)
			printf("%lli\n", sum[R]);
		else
			printf("%lli\n", sum[R] - sum[L - 1]);
	}
	return 0;
}
