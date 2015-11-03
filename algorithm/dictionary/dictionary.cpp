#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int n;
char words[200][20];
char sorting[26];

// 알파벳간에 관계 생성
void makeGraph(const char* word) { 
}


// 생성된 관계가 유효한지 체크
int valid_check() {
    int i, j;

    printf("debug\n");
    for(i=0; i < n; ++i) {
        printf("%c", sorting[i]);
    }
    printf("\n");

    for(i=0; i < n; ++i) {
        for(j=0; j < n; ++j) {
            if(sorting[i] == sorting[j] && i != j) {
                return -1;   
            }
        }
    }

    return 0;
}


void dictionary() {
    int i, j;

    for(i=0; i < n; ++i) {
        makeGraph(words[i]);
    }

    printf("reuslt\n");

    if(valid_check() == -1) {
        printf("INVALID HYPOTHESIS\n");

    } else {
        for(j=0; j < n; ++j) {
            printf("%c", sorting[j]);
        }
        printf("\n");
    }
}


int main(void) {
    int C;
    int i;
    scanf("%d", &C);

    for(;C--;) {
        scanf("%d", &n);

        for(i=0; i < n; ++i) {
            scanf("%s", words[i]); 
        }

        dictionary();
    }

    return 0;
}
