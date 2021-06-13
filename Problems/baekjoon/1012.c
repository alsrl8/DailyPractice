#include <stdio.h>

int T, M, N, K; // M : horizontal length, N : vertical length, K : number of cabbages
char field[50][50]; // 1 : place where cabbage planted in, 2 : place worms passed by

void move(int x, int y);

int main(){
    int T; // number of test cases
    int x, y; // location
    int worms; // number of worms needed
    
    scanf("%d", &T);
    for (int t = 0; t < T; t++){
		worms = 0;
		scanf("%d %d %d", &M, &N, &K);
		for (int i = 0; i < K; i++){
			scanf("%d %d", &x, &y);
			field[x][y] = '1';
		}

		for (int i = 0; i < M; i++)
			for (int j = 0; j < N; j++)
				if (field[i][j] == '1'){
					move(i, j);
					worms++;
				}

		printf("%d\n", worms);
	}
    return 0;   
}

void move(int x, int y){
	if (x == M || x < 0 || y == N || y < 0)
		return;

	if (field[x][y] != '1')
		return;

	field[x][y] = '2';
	K--;

	move(x + 1, y);
	move(x - 1, y);
	move(x, y + 1);
	move(x, y - 1);
}
