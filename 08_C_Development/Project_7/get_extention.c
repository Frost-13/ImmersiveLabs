#include <stdio.h>
#include <string.h>

int get_extension(const char *file_name);

int main(int argc, char*argv[])
{
const char *file_name = argv[1];
int number;

number = get_extension(file_name);
printf("%d\n", number);
return 0;
}

int get_extension(const char *file_name)
{
char *ext[5] = {".txt", ".out", ".bkp", ".dot", ".tx"};
//puts(file_name);
int length = strlen(file_name);
char extention[4];
int start;
for(int i =0; i<length; i++)
{
	if(file_name[i] == '.')
		start = i;
}
 
strncpy(extention, file_name+start, length-1);
//puts(extention);

for(int i=0; i<5; i++)
{
	if(strcmp(extention, ext[i]) == 0)
		return i;
}
return -1;
}
