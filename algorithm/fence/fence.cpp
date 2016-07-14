#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int arr[20000];

int fence(int left, int right) {
    if(left == right) return arr[left];

    int mid = (left + right) / 2;

    int ret = max(fence(left, mid), fence(mid+1, right));

    int lo = mid, hi = mid+1;
    int height = min(arr[lo], arr[hi]);
    
    ret = max(ret, height * 2);

    while(left < lo || hi < right) {
        if(hi < right && (lo == left || arr[lo-1] < arr[hi+1])) {
            ++hi;
            height = min(height, arr[hi]);

        } else {
            --lo;
            height = min(height, arr[lo]);
        }

        ret = max(ret, height * (hi-lo+1));
    }

    return ret;
}


int main(void) {
    int C;
    int N;
    int i;
    int h;

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
