#include <stdio.h>

int main(void) {
  int n, m, i, j, count=0;
  int arr[1001]={};
  for(i=1; i<=10; i++){
    scanf("%d", &n);
    arr[i]=n%42;
  }

  for(i=1;i<=10;i++){ 
    m=0;
    for(j=i+1; j<=10; j++){
      if(arr[i]==arr[j]) m++;
     } 
      if(m==0) count++;
  }
  printf("%d", count);
  return 0;
}