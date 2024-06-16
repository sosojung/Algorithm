#include <stdio.h>
int main(){
  int h, m, c;
  scanf("%d %d %d", &h, &m, &c);
  m += c;
  if(m > 59){
    h += m/60;
    m %= 60;
  }
  if(h > 23){
    h %= 24;
  }
  printf("%d %d", h, m);
  return 0;
}