#include <stdio.h>
#include <string.h>
int main()
{
	char message[101];


	printf("Enter a message: ");
	scanf("%[^\n]%*c", message);
	//puts(message);

	int length = strlen(message);
	//printf("%d", length);
	char *p = message + (length-1)/2;
	char *q = message;

	for(p = p; p >= q; p--)
	{
		printf("%c", *p);
	}
	printf("\n");
return 0;
}
