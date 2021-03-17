#ifndef __SQUEUE_H__
#define __SQUEUE_H__
#include <stdbool.h>

struct Node{
    char* val;
    struct Node* next;
    struct Node* prev;
};

typedef struct{
    struct Node* first;
    struct Node* last;
} Squeue;

void initSqueue (Squeue ** squeue);
bool isEmpty (const Squeue *squeue);
void addFront (Squeue *squeue, char* val);
void addBack (Squeue *squeue, char* val);
void leaveFront (Squeue *squeue);
char* peekBack (const Squeue *squeue);
void leaveBack (Squeue *squeue);
char* peekFront (const Squeue *squeue);
void print (const Squeue *squeue, char direction);
void nuke (Squeue *squeue);
void mergeFront(Squeue *squeue);
void mergeBack(Squeue *squeue);
void reverse(Squeue *squeue);
void destroySqueue(Squeue **squeue);
void terminate(const char *message);
#endif
