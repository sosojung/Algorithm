#include <stdio.h>

int main() {
    char c[101];
    int cnt = 0;
    scanf("%s", c);
    for(int i = 0; i < 101; i++) {
        if(c[i] != NULL) {
            cnt++;
        }
        else break;
    }
    printf("%d", cnt);
    return 0;
}