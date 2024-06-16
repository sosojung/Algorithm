#include <stdio.h>

int main(void) {
  int arr[101]={};
  int max=0, i, b=0;
  for(i=1; i<10; i++){
    scanf("%d", &arr[i]);
    if(arr[i] > max){ 
      max = arr[i];//최댓값 max에 저장
      b = i;//최댓값의 i값 b에 저장
    }
  }
  printf("%d\n", max);
  printf("%d", b);
  return 0;
}