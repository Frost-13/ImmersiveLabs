#include <stdio.h>
#define INT_BITS 32


unsigned int rotate_left(unsigned int i, int n){
   return (i << n)|(i >> (INT_BITS - n));
}


unsigned int rotate_right(unsigned int i, int n){
   return (i >> n)|(i << (INT_BITS - n));
}

int main(){
  unsigned int i;
  int n;

  printf("Enter number: ");
  scanf("%x", &i);

  printf("Enter number of bits to rotate: ");
  scanf("%d", &n);

  printf("Rotated left: 0x%x\n", rotate_left(i, n));
  printf("Rotated right: 0x%x\n", rotate_right(i, n));

  return 0;

}
