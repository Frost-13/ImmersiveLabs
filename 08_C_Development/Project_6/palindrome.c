#include <stdio.h>
#include <string.h>
#include <ctype.h>
int main()
{
	char message[101];
    printf("enter a message: ");
    scanf("%[^\n]%*c", message);
	//puts(message);
	
	int length = strlen(message);
	//printf("%d\n", length);
	
	char *e = message + length-1; // end of message
	char *s = message; //start of message
	//char *stop = message;
	while(e>s)
	{
		if((*s>='a' && *s<='z') || (*s>='A' && *s<='Z'))
		{
			if((*e>='a' && *e<='z') || (*e>='A' && *e<='Z'))
			{
				if(tolower(*s)!= tolower(*e))
				{	
					printf("Not a palindrome\n");
					return 0;
				}
				else
				{e--;
				s++;}
			}
			else
				e--;
		}
		else
			s++;
	}
	printf("Palindrome\n");
return 0;
}
