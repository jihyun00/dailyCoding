#include <iostream>
#include <algorithm>
#include <stdio.h>

using namespace std;

int arr[20000];

int fence(int left, int right) {
    int res;

    if(left == right) return h[left];

    int mid = (left+right)/2;

    res = max(fence(left, mid), fence(mid+1, right));
    
    
    // TODO
}


int main(void) {
    int C;
    int N;
    int i;

    scanf("%d", &C);

    for(;C--;) {
        scanf("%d", &N);

        for(i=0; i < N; ++i) {
            scanf("%d", &arr[i]); 
        }
        
        printf("%d\n", fence(0, N-1)); 
    }
    
    return 0;
}
