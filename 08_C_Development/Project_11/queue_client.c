#include <stdio.h>
#include <stdlib.h>
#include "queue.h"
int main(void){
	int key = 1;
	int item;
	Queue qu;
	qu = create();
	while(1)
	{
		printf("Enter the operation:");
		scanf("%d", &key);

		if (key==1)
		{
			printf("Enter item to enter: ");
			scanf("%d", &item);
			insert(qu, item);
		}

		if (key==2)
			remove_first(qu);

		if (key==3)
			Display_FirstItem(qu);

		if (key==4)
			Display_LastItem(qu);

		if (key==5)
			printq(qu);

		if (key==6)
			is_empty(qu);

		if (key==7)
			delete_from_list(qu);

		if (key == 0)
			break;
	}
	free(qu);
	return 0;
}
