#include <stdio.h>

int main() {
    int n;
    scanf("%d", &n);
    int a, b, x;
    for(int i = 1; i <= n; i++) {
        scanf("%d%d%d", &a, &b, &x);
        printf("%d\n", a*(x-1)+b);
    }
    return 0;
}