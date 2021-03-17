#include "squeue.h"
#include <assert.h>
#include <string.h>
#include <stdlib.h>

int main()
{
  Squeue *s1 = NULL;
  initSqueue(&s1);
  //Squeue should be empty
  assert(isEmpty(s1));
  addFront(s1, "Hello");
  //We just added "Hello", so it shouldn't be empty
  assert(!isEmpty(s1));
  addBack(s1, "World!");
  //We should have "Hello", "World!" in the Squeue in that order.
  assert(strcmp(peekFront(s1), "Hello") == 0);
  assert(strcmp(peekBack(s1), "World!") == 0);
  //We are going to merge "Hello" with "World!"
  mergeFront(s1);
  assert(strcmp(peekFront(s1), "HelloWorld!") == 0);
  //We have only one element so the front and back of the squeue should be equal
  assert(strcmp(peekFront(s1), peekBack(s1)) == 0);
  addFront(s1, "Hola");
  addBack(s1, "Mundo!");
  print(s1, 'f');
  reverse(s1);
  print(s1, 'r');
  assert(strcmp(peekFront(s1), "Mundo!") == 0);
  assert(strcmp(peekBack(s1), "Hola") == 0);
  leaveFront(s1);
  assert(strcmp(peekFront(s1), "HelloWorld!") == 0);
  nuke(s1);
  //We just nuked our Squeue, so it should be empty
  assert(isEmpty(s1));
  destroySqueue(&s1);
  return 0;
}
