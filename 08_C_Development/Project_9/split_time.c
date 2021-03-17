#include <stdio.h>
#include <stdlib.h>

typedef struct
{
 int hours;
 int minutes;
 int seconds;
}time;

time split_time(long total_seconds);


int main()
{

 int total_seconds;
 time answer;

 printf("Enter time as seconds since midnight: ");
 scanf("%d", &total_seconds);

 //printf("%d\n", total_seconds);

 answer = split_time(total_seconds);

 printf("  Hours: %d\nMinutes: %d\nSeconds: %d\n", answer.hours, answer.minutes, answer.seconds);
 return 0;
}


time split_time(long total_seconds)
{
  //printf("%ld\n", total_seconds);
  /*
  int hours = ((total_seconds/60)/60);
  int minutes = (total_seconds/60);
  int seconds = (total_seconds%60);
  */

  time answer;
  answer.hours = ((total_seconds/60)/60);
  answer.minutes = (total_seconds/60)- (answer.hours*60);
  answer.seconds = (total_seconds%60);

  return answer;
}
