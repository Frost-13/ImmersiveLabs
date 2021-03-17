#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

#define STACK_SIZE 6

/* external variables */
char contents[STACK_SIZE];
int top = 0;

void make_empty(void){
    top = 0;
}

bool is_empty(void){
    return top == 0;
}

bool is_full(void){
    return top == STACK_SIZE;
}

void push(char i){

    if (is_full())
        printf("STACK OVERFLOW\n");
		exit(5);

    else
        contents[top++] = i;
}

char pop(void){
    
    if (is_empty())
        printf("STACK UNDERFLOW");
		exit(4);
    else
        return contents[--top];
}
