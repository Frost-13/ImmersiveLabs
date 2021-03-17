#include <stdio.h>
#include <stdlib.h>
#include "queue.h"

struct node{
	int data;
	struct node *next;
};

struct queue_type{
	struct node *first;
	struct node *last;
};

Queue create(void)
{
	Queue qu = malloc(sizeof(struct queue_type));
	if(qu == NULL)
	{
		printf("error in create");
		exit(EXIT_FAILURE);
	}
	qu->first =NULL;
	qu->last = NULL;
	return qu;
}

void insert(Queue qu, int i)
{
	struct node *new_node = malloc(sizeof(struct node));
	new_node->data = i;
	new_node->next = NULL;

	if (new_node == NULL)
		{
		printf("Error in insert: Queue is full.");
		exit(EXIT_FAILURE);
	}
	if (qu->last==NULL)
		{
			qu->last = new_node;
		  qu->first = new_node;
			printf("HELLO");
		}

	else
	{
		qu->last->next= new_node;
		qu->last = new_node;
	}

}

void remove_first(Queue qu)
{
	if(qu->first == NULL)
		printf("CAN'T REMOVE NULL TYPE");
	else{
		struct node *temp = qu->first->next;
		free(qu->first);
		qu->first = temp;
	}

}
void Display_FirstItem(Queue qu)
	{
		int temp = qu->first->data;
		printf("%d\n", temp);
	}

void Display_LastItem(Queue qu)
{
	int temp = qu->last->data;
	printf("%d\n", temp);
}

bool is_empty(Queue qu)
{
	if(qu->first ==NULL && qu->last==NULL){
		printf("Empty\n");
		return 1;
	}
	else
		printf("not Empty\n");
		return 0;
}

void delete_from_list(Queue qu)
{
		struct node *p;

		while(qu->first !=NULL)
		{
			p = qu->first;
			qu->first = qu->first->next;
			free(p);
		}
}

void printq(Queue qu)
{
		struct node *p;
		p = qu->first;
		while(p !=NULL)
		{
			printf("%d\n", p->data);
			p = p->next;
		}
}
