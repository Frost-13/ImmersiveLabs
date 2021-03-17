#ifndef QUEUE_H
#define QUEUE_H
#include <stdbool.h>

typedef int Item;

typedef struct queue_type *Queue;

Queue create(void);
void insert(Queue qu, int item);
void remove_first(Queue qu);
void Display_FirstItem(Queue qu);
void Display_LastItem(Queue qu);
void printq(Queue qu);
bool is_empty(Queue qu);
void delete_from_list(Queue qu);

#endif
