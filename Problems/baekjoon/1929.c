#include <stdio.h>
#include <math.h>

int isPrimeNumber(int num);

int main(){
    int M, N;
    scanf("%d %d", &M, &N);
    for(int i = M ; i <= N ; i ++)
        if(isPrimeNumber(i))
            printf("%d\n", i);
    return 0;
}

int isPrimeNumber(int num){
    if(num < 2)
        return 0;
    int len = (int)sqrt(num);
    for(int i = 2 ; i <= len; i ++)
        if(num % i == 0)
            return 0;
    return 1;
}
