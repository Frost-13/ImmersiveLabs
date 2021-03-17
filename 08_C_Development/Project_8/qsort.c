/* Sorts an array of integers using Quicksort algorithm */
/* Copyright K.N. King -- C programming Ch9.6 */

#include <stdio.h>
#include "quicksort.h"

#define N 10

int main(void){

    int a[N], i;

    printf("Enter %d numbers to be sorted: ", N);
    for(i = 0; i < N; i++)
        scanf("%d", &a[i]);

    quicksort(a, &a[0], &a[N - 1]);

    printf("In sorted order: ");
    for (i = 0; i < N; i++)
        printf("%d ", a[i]);

    printf("\n");

    return 0;
}