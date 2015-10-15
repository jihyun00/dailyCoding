#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <vector>

int n;
char words[200][20];

vector<vector<int> > adj;

void makeGraph(const vector<string>& word) {
    adj = vecotr<vector<int> >(26, vector<int>(26, 0));
    for(int j = 1; j < words.size(); ++j) {
        int i = j-1, len = min(word[i].size(), word[j].size());

        for(int k = 0; k < len; ++k) {
            if(word[i][k] != word[j][k]) {
                int a = words[i][k] - 'a';
                int b = words[j][k] - 'a';
                adj[a][b] = 1;
                break;
            }
        }
    }
}


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
