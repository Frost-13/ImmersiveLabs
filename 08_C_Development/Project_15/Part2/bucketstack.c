/***
* CMPUT 201 Assignment License
* Version 1.0
*
* Copyright 2018 Sarah Nadi
* Unauthorized redistribution is forbidden under all circumstances. Use of this
* software without explicit authorization from the author **and** the CMPUT 201
* Instructor is prohibited.
* This software was produced as part of an assignment in the course
* CMPUT 201 - Practical Programming Methodology at the University of
* Alberta, Canada. This code is confidential and remains confidential
* after it is submitted for grading. The course staff has the right to
* run plagiarism-detection tools on any code developed under this license,
* even beyond the duration of the course.
*
* Copying any part of this code without including this copyright notice
* is illegal.
*
* If any portion of this software is included in a solution submitted for
* grading at an educational institution, the submitter will be subject to
* the plagiarism sanctions at that institution.
*
* This software cannot be publicly posted under any circumstances, whether by
* the original student or by a third party.
* If this software is found in any public website or public repository, the
* person finding it is kindly requested to immediately report, including
* the URL or other repository locating information, to the following email
* address:
*
*          nadi@ualberta.ca
***/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <assert.h>
#include "bucketstack.h"
#include <stdbool.h>


// This function creates a new bucket
struct NodeBucket* createNewNodeBucket (int bucketSize){
  if(bucketSize == 0)
    terminate("Bucket size cannot be 0");

  struct NodeBucket* new_buc = malloc(sizeof(struct NodeBucket));

  if(new_buc == NULL)
    terminate("Error in createNewNodeBucket");

  new_buc->val = malloc(sizeof(char*)*bucketSize);
  if(new_buc->val == NULL)
    terminate("Error in createNewNodeBucket");

  return new_buc;
}
// This function creates a new stack
void initStack (int bucketSize, Stack **stack){
  *stack = malloc(sizeof(Stack));

  if(*stack == NULL)
    terminate("Error in initStack");

  (*stack)->firstBucket = NULL;
  // i made this -1 because there are no elements in the bucket when something gets added then it has index 0 and the size gets updated to 0
  (*stack)->topElt = -1;
  (*stack)->bucketSize = bucketSize;
}

// Checks to see if stack is empty
bool isEmpty (const Stack *stack){
  if(stack->firstBucket ==NULL)
    return 1;
  else
    return 0;
}

// puts the given val into the top of the bucket
void push (char* val, Stack *stack){
  assert(stack!=NULL);

  char* value = malloc(strlen(val)+1);
  if (value == NULL)
    terminate("Error in push");

  strcpy(value,val);
  if(stack->topElt == stack->bucketSize -1 || stack->topElt == -1){
      struct NodeBucket* new_buck = createNewNodeBucket(stack->bucketSize);

      new_buck->next = stack->firstBucket;
      new_buck->val[0] = value;

      stack->topElt = 0;
      stack->firstBucket = new_buck;
  }
  else{
      stack->topElt += 1;
      stack->firstBucket->val[stack->topElt] = value;
  }
}

// removes the top element in the bucket
void pop(Stack *stack){
    assert(!isEmpty(stack));

    if(stack->topElt == 0){
        struct NodeBucket* temp_buck = stack->firstBucket;
        stack->firstBucket = temp_buck->next;

        if(stack->firstBucket!=NULL)
          stack->topElt = stack->bucketSize -1;
        else
          stack->topElt = -1;

        free(temp_buck->val[0]);
        free(temp_buck->val);
        free(temp_buck);
    }
    else{
      free(stack->firstBucket->val[stack->topElt]);
      stack->topElt -= 1;
    }
}

// returns the size of the current bucket
int size (const Stack *stack){
  assert(stack!=NULL);

  if(stack->topElt == -1)
    return 0;

  struct NodeBucket* buck = stack->firstBucket;
  int answer = 0;

  while(buck!= NULL){
      answer++;
      buck = buck->next;
  }
  answer = (answer-1)*stack->bucketSize;
  answer = answer + stack->topElt + 1;

  return answer;
}

// returns top element in the bucket
char* top (const Stack *stack){
  assert(!isEmpty(stack));
  return stack->firstBucket->val[stack->topElt];
 }

// swaps top 2 elements in the bucket 
void swap (Stack *stack){
  assert(!isEmpty(stack));
  if(stack->firstBucket->val[stack->topElt] == NULL || stack->firstBucket->val[stack->topElt-1] ==NULL)
    terminate("Less than 2 elements in bucket.");

  char *first = stack->firstBucket->val[stack->topElt];
  char *second = stack->firstBucket->val[stack->topElt-1];

  stack->firstBucket->val[stack->topElt] = second;
  stack->firstBucket->val[stack->topElt-1] = first;
}
// prints all elements
void print (const Stack *stack){
  assert(stack!=NULL);

  struct NodeBucket* buck = stack->firstBucket;
  if(stack->topElt == -1)
    terminate("Error bucket is empty");

  printf("stack is:\n");
  int i = stack->topElt;
  while(buck != NULL){

    while(i>=0){
      printf("\t%s\n",buck->val[i]);
      i--;
      }
    i = stack->bucketSize -1; //communications security establishment
    buck = buck->next;
  }
}

// deletes all elements in bucket but not the stack itself. frees all mallocked memory 
void clear(Stack *stack){
  assert(stack!=NULL);

  struct NodeBucket* buck = stack->firstBucket;

  if(stack->topElt == -1)return;

  int i = stack->topElt;
  while(buck != NULL){

    while(i>=0){
      free(buck->val[i]);
      i--;
    }

    free(buck->val);
    i = stack->bucketSize -1;

    struct NodeBucket* prev = buck;
    buck = buck->next;
    free(prev);
  }
  stack->topElt = -1;
}
// delets all items in the buckets by calling clear. then delets the stack and frees memory
void destroyStack(Stack **stack){ //defcon videos
  clear(*stack);
  free(*stack);
  *stack = NULL;
}

// same as part 1
void terminate(const char *message){
  printf("%s\n", message);
  exit(EXIT_FAILURE);
}
