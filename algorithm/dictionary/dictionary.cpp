#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <string>
#include <vector>

using namespace std;

int n;

vector<vector<int> > adj;

void makeGraph(const vector<string>& words) { // TODO : comprehension
    adj = vector<vector<int> >(26, vector<int>(26, 0)); // vector 안에 vector? adj의 역할?
    for(int j = 1; j < words.size(); ++j) { // scanf로 입력받은 words의 갯수 -> n이겠네
        int i = j-1, len = min(words[i].size(), words[j].size()); // 

        // words[i]가 words[j] 앞에 오는 이유를 찾는다
        for(int k = 0; k < len; ++k) {
            if(words[i][k] != words[j][k]) {
                int a = words[i][k] - 'a'; // int 만들려고 -> 왜 int 만들려고?
                int b = words[j][k] - 'a'; // 
                adj[a][b] = 1; // 이 부분을 왜 하는지 이해가 안 감;
                break;
            }
        }
    }
}


vector<int> seen, order;
void dfs(int here) { 
    seen[here] = 1; // 봤던 걸 1 로 설정하는 듯
    for(int there = 0; there < adj.size(); ++there) 
        if(adj[here][there] && !seen[there])  
            dfs(there);
    order.push_back(here);
}


vector<int> topologicalSort() { // TODO: Comprehension
    int n = adj.size();
    seen = vector<int>(n, 0);
    order.clear();
    for(int i=0; i < n; ++i) if(!seen[i]) dfs(i);
    reverse(order.begin(), order.end()); // reverse 함수-> 다 순서 뒤집음
    for(int i = 0; i < n; ++i)
        for(int j = i+1; j < n; ++j)
            if(adj[order[j]][order[i]])
                return vector<int>();

    return order;
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
            scanf("%s", words[i]); // words[i] push_back() 함수 적용
        }

        dictionary();
    }

    return 0;
}
