#include <stdio.h>

int count_ones(unsigned char ch){
  int count = 0, i;
  for(i=0; i<8; i++){
    if((ch>>i) & 1){
      count++;
    }
  }
  return count;

}

int main(){
  unsigned char let[3];
  while(1){

    printf("Enter character: ");
    fgets((char *)let, 3, stdin);
    //fflush(stdin);

    if(let[0] == 'x'){
      break;
    }

    else{
      printf("Number of 1 bits in %c is: %d\n", let[0], count_ones(let[0]));
    }
  }
  return 0;
}
