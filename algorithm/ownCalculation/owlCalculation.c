#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int quart(int N, int target) {
    int i;
    for(i=0; i < N; ++i) {
        target *= target;
    }

    return target;
}

void owlCalculation(const int num) {
    int i, j;
    int quo = 0;
    int sum_quo = 0;
    int sum_digit = 0;

    for(i=0; i < 5; ++i) {
        quo = num / quart(i, 10);

        if(quo == 0) { // i-1한 값까지 유효
            break;
        }
    }

    for(j=0; j < i-1; ++j) {
        // TODO
    }

    printf("sum : %d\n", sum_digit);

}

int main(void) {
    char *words;
    int N;

    while(1) {
        scanf("%s", words);

        if(strcmp(words, "END") == 0) {
            break;

        } else {
            N = atoi(words);
            owlCalculation(N);
        }
    }

    return 0;
}
