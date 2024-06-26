#include <stdio.h>

int main() {
    int n, m;
    for(int i = 0;;i++) {
        scanf("%d%d", &n, &m);
        if(n == 0 && m == 0) break;
        printf("%s\n", n > m ? "Yes" : "No");
    }
    return 0;
}