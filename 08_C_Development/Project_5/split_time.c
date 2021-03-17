#include <stdio.h>
#include <stdlib.h>

void split_time(long total_sec, int *hr, int *min, int *sec);

int main(int argc, char *argv[])
{
	long total_sec = atoi(argv[1]);
	
	int hr, min, sec;
		
	split_time(total_sec, &hr,&min, &sec);
	
	printf("Converted time = %.2d:%.2d:%.2d\n", hr, min, sec);
 
return 0;
}


void split_time(long total_sec, int *hr, int *min, int *sec)
{	
	*sec = total_sec % 60;
	
	int temp_min = total_sec /60; 
	*min = temp_min % 60;

	*hr = total_sec / 3600;


	
return;
}
