#include <stdio.h>
#include <string.h>

void quadtree(char *val, char *res) {
    memset(res, 0, sizeof(res));

}


int main(void) {
    int C;
    char val[1000];
    char res[1000];

    scanf("%d", &C);

    for(;C--;) {
        memset(val, 0, sizeof(val));

        scanf("%s", val);

        quadtree(val, res);
    }

    return 0;
}
