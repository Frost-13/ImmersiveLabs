#include "stack.h"
#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

int main()
{
	char temp;
	char string[6];
	printf("enter parentheses and/or backets: ");
	scanf("%s", string);
	
	for(int i=0; i<= strlen(string); i++)
	{
		if(string[i] == '(' || string[i] == '{')
			push(string[i]);
		
		if(string[i] ==')' || string[i] == '}')
		{	
			temp = pop();			
			if(temp == string[i])
				continue;
			else
			{
				push(temp);
				push(string[i]);
			}
		}
	}

if(is_empty())
	printf("parentheses are nested properly");

else
	printf("parentheses are not nested properly");


return 0;
}
