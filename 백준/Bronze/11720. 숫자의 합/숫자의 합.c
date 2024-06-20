#include <stdio.h>

int main() {
    int n, sum = 0;
    char number[101]; // 숫자가 공백없이 입력되기 때문
    scanf("%d%s", &n, number);
    for(int i = 0; i < n; i++) {
        sum += number[i] - '0'; // 문자를 숫자로 변환하는 과정에서 아스키코드로 의해 0~9의 수는 48~57까지의 숫자로 변환된다. 그래서 '0' 또는 48을 뺴줘야 함.
    }
    printf("%d", sum);
    return 0;
}