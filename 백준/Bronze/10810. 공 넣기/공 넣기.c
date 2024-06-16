#include <stdio.h>

int main(void) {
  int n, m, g, h, i, j, k;
  int arr[101]={};
  scanf("%d %d", &n, &m);
  for(g=1; g<=m; g++){
    scanf("%d %d %d", &i, &j, &k);
    for(i=i; i<=j; i++){
      arr[i] = k;
    }
  }
  for(h=1; h<=n; h++){//n만 출력하면 값이 고정이니까 포문 돌려서
    printf("%d ", arr[h]);
  }
  return 0;
}