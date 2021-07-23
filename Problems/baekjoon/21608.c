#include <stdio.h>

int N;
int room[20][20];
int num_of_blanked[20][20];
int prefer[401][4];

int dRow[4] = { 1, -1, 0, 0 };
int dCol[4] = { 0, 0, 1, -1 };

typedef struct{
	int r, c;
}POS;

void init(){
	for (int c = 0; c < N; c++){
		num_of_blanked[0][c] = 3;
		num_of_blanked[N - 1][c] = 3;
	}
	for (int r = 0; r < N; r++){
		num_of_blanked[r][0] = 3;
		num_of_blanked[r][N - 1] = 3;
	}
	for (int r = 1; r < N - 1; r++)
		for (int c = 1; c < N - 1; c++)
			num_of_blanked[r][c] = 4;
	num_of_blanked[0][0] = 2;
	num_of_blanked[0][N - 1] = 2;
	num_of_blanked[N - 1][0] = 2;
	num_of_blanked[N - 1][N - 1] = 2;
}

int get_number_of_prefer(int stu, int row, int col){
	int newR, newC;
	int cnt = 0;

	for (int d = 0; d < 4; d++){
		newR = dRow[d] + row;
		newC = dCol[d] + col;
		if (newR < 0 || newR >= N || newC < 0 || newC >= N) continue;
		for (int i = 0; i < 4; i++)
			if (room[newR][newC] == prefer[stu][i])
				cnt++;
	}
	return cnt;
}

POS get_pos(int stu){
	int cnt_prefer = -1;
	int cnt_blanked = -1;
	int temp;
	POS pos;
	
	for (int r = 0; r < N; r++)
		for (int c = 0; c < N; c++){
			if (room[r][c] > 0) continue;
			temp = get_number_of_prefer(stu, r, c);
			if (temp > cnt_prefer){
				cnt_prefer = temp;
				cnt_blanked = num_of_blanked[r][c];
				pos.r = r;
				pos.c = c;
			}
			else if (temp == cnt_prefer && num_of_blanked[r][c] > cnt_blanked){
				cnt_blanked = num_of_blanked[r][c];
				pos.r = r;
				pos.c = c;
			}
		}
	return pos;
}

int main(){
	int stu;
	int newR, newC;
	int answer = 0;
	int scores[] = { 0, 1, 10, 100, 1000 };
	POS pos;
	
	scanf("%d", &N);
	init();
	for (int i = 0; i < N * N; i++){
		scanf("%d", &stu);
		for (int j = 0; j < 4; j++)
			scanf("%d", &prefer[stu][j]);
		
		pos = get_pos(stu);
		room[pos.r][pos.c] = stu;
		for (int d = 0; d < 4; d++){
			newR = dRow[d] + pos.r;
			newC = dCol[d] + pos.c;
			if (newR < 0 || newR >= N || newC < 0 || newC >= N) continue;
			num_of_blanked[newR][newC]--;
		}
	}

	for (int r = 0; r < N; r++)
		for (int c = 0; c < N; c++)
			answer += scores[get_number_of_prefer(room[r][c], r, c)];
	printf("%d", answer);

	return 0;
}
