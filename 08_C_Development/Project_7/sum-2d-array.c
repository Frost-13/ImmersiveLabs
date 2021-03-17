#include <stdio.h>
#include <string.h>
#define LEN 10
int sum_two_dimensional_array(const int (*p)[LEN], int n);


int main()
{
int (*p)[LEN];
int numbers[2][LEN] = {{1,2,3,4,5,6,7,8,9,10}, 
						{2,3,4,5,6,7,8,9,10,11}};

int num;
p= numbers;

num = sum_two_dimensional_array(p++,2);
printf("The sum of all elements of the array is: %d\n", num);
return 0;
}


int sum_two_dimensional_array(const int (*p)[LEN], int n)
{

 int *q;
 q = (int*)p;

 int i, sum = 0;

 for (i = 0; i < n*LEN; i++)
   sum += *(q+i);

 return sum;
}
