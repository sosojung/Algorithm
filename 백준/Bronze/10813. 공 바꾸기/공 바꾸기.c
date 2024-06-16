#include <stdio.h>

int main(void) {
  int n, m;
  int temp, g, h, i, j;
  int arr[101]={};
  scanf("%d %d", &n, &m);
  for(h=1; h<=n; h++){
    arr[h]=h;
  }
  for(g=1; g<=m; g++){
    scanf("%d %d", &i, &j);
    temp = arr[i];
    arr[i] = arr[j];
    arr[j] = temp;
  }
  for(h=1; h<=n; h++){
    printf("%d ", arr[h]);
  }
  return 0;
}