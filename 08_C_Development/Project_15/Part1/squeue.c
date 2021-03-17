#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <assert.h>
#include "squeue.h"

// creates the squeue
void initSqueue (Squeue ** squeue){
    *squeue = malloc(sizeof(Squeue));
    if (*squeue!= NULL) {
        (*squeue)->first = NULL;
        (*squeue)->last = NULL;
    }
    else
        terminate("initSqueue failed");

}

// checks to see if given squeue is empty
bool isEmpty (const Squeue *squeue){
    if (squeue->first == NULL && squeue->last == NULL)
        return 1;
    else
      return 0;

}

// Adds a given char to the squeue
void addFront (Squeue *squeue, char *val){
    char* new_val = malloc(strlen(val)+1);
    if (new_val == NULL)
        terminate("addFront failed");

    strcpy(new_val,val);
    struct Node* new_first = malloc(sizeof(struct Node));


    if (new_first != NULL){
        new_first->val = new_val;
        new_first->next = squeue->first;
        if(squeue->first != NULL){
            squeue->first->prev = new_first;
            new_first->prev = NULL;
        }
        else
            new_first->prev = NULL;
    }

    else
        terminate("addFront failed");

    squeue->first = new_first;
    if(squeue->last == NULL)
        squeue->last = new_first;

}

// Adds a given char to the back of the squeue
void addBack (Squeue *squeue, char *val){
    char* new_val = malloc(strlen(val)+1);
    if (new_val == NULL)
        terminate("addBack failed");

    strcpy(new_val,val);
    struct Node* new_last = malloc(sizeof(struct Node));


    if (new_last != NULL){
        new_last->val = new_val;
        new_last->prev = squeue->last;
        if(squeue->last != NULL){
            squeue->last->next = new_last;
            new_last->next = NULL;
        }
        else
            new_last->next = NULL;
    }
    else
        terminate("addBack failed");

    squeue->last = new_last;

    if(squeue->first == NULL){
        squeue->first = new_last;
    }
}

// If r is called print all items in the squeue backwards(in reverse order)
// if f is called print all items in the squeue forwards
void print (const Squeue *squeue, char direction){
    if (direction == 'f'){
        printf("stack is:\n");
        struct Node *temp_node = squeue->first;
        while (temp_node != NULL){
            printf("\t%s\n",temp_node->val);
            temp_node = temp_node->next;
        }
    }
    else if(direction == 'r'){
        printf("stack is:\n");
        struct Node *temp_node = squeue->last;
        while (temp_node != NULL){
            printf("\t%s\n",temp_node->val);
            temp_node = temp_node->prev;
        }
    }
    else
        terminate("Invalid direction");
}

// delete all items in the squeue but not the squeue itself. frees all the memory of the malloced items
void nuke (Squeue *squeue){
    while (squeue->first != NULL){
        struct Node *temp_node = squeue->first;
        squeue->first = squeue->first->next;
        free(temp_node->val);
        free(temp_node);
    }
    squeue->last = NULL;
}

// delete the first element in the squeue 
void leaveFront (Squeue *squeue){
    assert (!isEmpty(squeue));
    struct Node* old_top;

    old_top = squeue->first;
    squeue->first = squeue->first->next;
    squeue->first->prev = NULL;

    free(old_top->val);
    free(old_top);

    if(squeue->first == NULL){
        squeue->last = NULL;
    }
}

// Deletes the last element in the squeue
void leaveBack (Squeue *squeue){
    assert (!isEmpty(squeue));
    struct Node* old_btm;

    old_btm = squeue->last;
    squeue->last = squeue->last->prev;
    squeue->last->next = NULL;

    free(old_btm->val);
    free(old_btm);

    if(squeue->last == NULL){
        squeue->first = NULL;
    }
}

// shows (returns) the first element in the squeue
char* peekFront (const Squeue *squeue){
    assert (!isEmpty(squeue));
    return squeue->first->val;
}

// returns last element in the squeue
char* peekBack (const Squeue *squeue){
    assert (!isEmpty(squeue));
    return squeue->last->val;
}

// Changes the order of the squeue elements
void reverse(Squeue *squeue){
    assert (!isEmpty(squeue));
    struct Node* temp_node = squeue->first;

    while(temp_node!=NULL){
        struct Node* swap = temp_node->prev;
        temp_node->prev = temp_node->next;
        temp_node->next = swap;
        temp_node = temp_node->prev;
      }

    temp_node = squeue->first;
    squeue->first = squeue->last;
    squeue->last = temp_node;
}


// makes the forst 2 elements into one element
void mergeFront(Squeue *squeue){
    assert(squeue->first != squeue->last);
    squeue->first->val = realloc(squeue->first->val,strlen(squeue->first->val)+strlen(squeue->first->next->val)+2);

    if (squeue->first->val == NULL)
        terminate("mergeFront failed");

    strcat(squeue->first->val,squeue->first->next->val);
    struct Node* temp_node = squeue->first;
    free(squeue->first->next->val);
    squeue->first->next->val = squeue->first->val;
    squeue->first = squeue->first->next;

    free(temp_node);
}

// Makes the last 2 elements into one element as the very end of the squeue
void mergeBack(Squeue *squeue){
    assert(squeue->first != squeue->last);
    squeue->last->prev->val = realloc(squeue->last->prev->val,strlen(squeue->first->val)+strlen(squeue->first->next->val)+2);

    if (squeue->last->prev->val == NULL)
        terminate("mergeBack failed");

    strcat(squeue->last->prev->val,squeue->last->val);
    struct Node* temp_node = squeue->last;
    squeue->last = squeue->last->prev;
    free(temp_node->val);
    free(temp_node);
}

// remove all items in the squeue by calling nuke then deleting the squeue itself. frees the memory that the squeue was using
void destroySqueue(Squeue **squeue){
    nuke(*squeue);
    free(*squeue);
    *squeue = NULL;
}

// just a print statment and exit condition. this gets called if something goes wrong
void terminate(const char *message){
  printf("%s\n", message);
  exit(EXIT_FAILURE);
}
