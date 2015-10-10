#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <vector>

int n;
char words[200][20];

void dictionary() {
        
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
    }

    return 0;
}
