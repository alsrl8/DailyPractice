#include <stdio.h>
#include <string.h>
#define MAX 51

int N, M, T;
int x[MAX], d[MAX], k[MAX]; // d (0:clockwise, 1:counter-clockwise), 1<=k<M
int C[MAX][MAX]; // { number of circle, index of number }
int idxTop[MAX]; // index of each circle's top

void turn(int numC, int dir, int cnt){
	if (dir == 0){ // clockwise
		idxTop[numC] -= cnt;
		idxTop[numC] = (idxTop[numC] + M) % M;
	}
	else{ // counter-clockwise
		idxTop[numC] += cnt;
		idxTop[numC] %= M;
	}
}

void remove_number(){
	int check[MAX][MAX], cntRemove = 0;
	int cntNum = 0, sum = 0;
	double avg;
	memset(check, 0, sizeof(check));

	for (int n = 1; n < N; n++){
		for (int i = 0; i < M; i++){
			if (C[n][(idxTop[n] + i) % M] == C[n + 1][(idxTop[n + 1] + i) % M]){
				check[n][(idxTop[n] + i) % M] = 1;
				check[n + 1][(idxTop[n + 1] + i) % M] = 1;
			}
		}
	}

	for (int n = 1; n <= N; n++){
		for (int i = 0; i < M - 1; i++){
			if (C[n][i] == C[n][i + 1]){
				check[n][i] = 1;
				check[n][i + 1] = 1;
			}
		}
		if (C[n][M - 1] == C[n][0]){
			check[n][0] = 1;
			check[n][M - 1] = 1;
		}
	}

	for (int i = 1; i <= N; i++)
		for (int j = 0; j < M; j++)
			if (check[i][j] == 1 && C[i][j] > 0){
				C[i][j] = 0;
				cntRemove++;
			}

	if (cntRemove == 0){
		for (int i = 1; i <= N; i++)
			for (int j = 0; j < M; j++){
				if (C[i][j] > 0){
					cntNum++;
					sum += C[i][j];
				}
			}
		avg = (double)sum / cntNum;

		for (int i = 1; i <= N; i++)
			for (int j = 0; j < M; j++){
				if (C[i][j] > 0){
					if (C[i][j] < avg)
						C[i][j] ++;
					else if (C[i][j] > avg)
						C[i][j]--;
				}
			}
	}
}

int get_sum(){
	int sum = 0;
	for (int i = 1; i <= N; i++)
		for (int j = 0; j < M; j++){
			if (C[i][j] > 0){
				sum += C[i][j];
			}
		}
	return sum;
}

int main(){
	scanf("%d %d %d", &N, &M, &T);
	for (int i = 1; i <= N; i++)
		for (int j = 0; j < M; j++)
			scanf("%d", &C[i][j]);
	for (int t = 0; t < T; t++)
		scanf("%d %d %d", &x[t], &d[t], &k[t]);

	for (int t = 0; t < T; t++){
		for (int i = 1; i*x[t] <= N; i++)
			turn(i * x[t], d[t], k[t]);
		remove_number();
	}
	printf("%d", get_sum());
	return 0;    
}
