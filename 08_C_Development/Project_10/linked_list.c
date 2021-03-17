#include <stdio.h>
#include <stdlib.h>
#include "linked_list.h"

struct node *add_to_list(struct node *list, int n, char marker){
	struct node *new_node;
	new_node = malloc(sizeof(struct node));

	if(new_node == NULL){
		printf("Error: malloc failed in add_to_list\n");
		exit(EXIT_FAILURE);
	}

	new_node->value = n;
	new_node->marker = marker;
	new_node->next = list;


	return new_node;

}

struct node *find_last(struct node *list, int n){

	struct node *p =NULL;
	for(;list!=NULL; list = list->next){
		if(list->value == n){
			p = list;
			}
		}
		return p;
		}

void delete_from_list(struct node *list){
		struct node *p;

		while(list!=NULL)
		{
			p=list;
			list=list->next;
			free(p);
		}
	}
