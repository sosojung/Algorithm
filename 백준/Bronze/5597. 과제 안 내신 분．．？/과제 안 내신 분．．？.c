#include <stdio.h>

int main(void) {
  int n, m, o, i;
  int arr[31]={};
  for(i=1; i<=28; i++){
    scanf("%d", &n);
    arr[n]=1;
  }
  for(i=1; i<=30; i++){      
    if(arr[i]==0) printf("%d\n", i);
  }
  return 0;
}