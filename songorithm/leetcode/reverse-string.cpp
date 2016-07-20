#include <stdio.h>
#include <string.h>
#include <stdlib.h>


char *reverse(char *val) {
    char *res;
    int len;
    int j;

    len = strlen(val);

    j = len-1;

    res = (char *)malloc(len);

    for(int i=0; i < len; ++i) {
        res[i] = val[j--];
    }

    return res;
}


int main(void) {
    char *input = "hello";
    char *res;

    res = reverse(input);

    printf("%s\n", res);


    return 0;
}
