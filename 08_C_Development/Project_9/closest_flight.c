#include <stdio.h>
#include <stdlib.h>
typedef struct
{
  int departure;
  int arrival;
}flight;

int main()
{
  flight flight1,flight2,flight3,flight4;
  flight1.departure = 480;
  flight1.arrival = 616;

  flight2.departure = 583;
  flight2.arrival = 712;

  flight3.departure = 679;
  flight3.arrival = 811;

  flight4.departure = 762;
  flight4.arrival = 900;

  flight flights[4] = {flight1, flight2, flight3, flight4};
  //int times[] = (480, 615, 583, 712)
  int hour, min, user_time, i, diff= 10000000, temp, answer;
  printf("Enter a 24-hour time: ");
  scanf("%d:%d", &hour, &min);

  user_time = (hour*60)+min;

  printf("%d\n", user_time);
  for(i=0; i<4; i++)
    {
      //printf("%d\n", flights[i].departure);
      temp = abs(flights[i].departure - user_time);

      if(temp< diff)
      {
        diff = temp;
        //printf("%d\n", i);
        answer= i;
      }
    }

  if(answer == 0)
  {
    printf("Closest departure time is 08:00 a.m, arriving at 10:16 p.m.");
  }

  if(answer == 1)
  {
    printf("Closest departure time is 9:43 a.m, arriving at 11:52 p.m.");
  }

  if(answer == 2)
  {
    printf("Closest departure time is 11:19 a.m, arriving at 1:31 p.m.");
  }

  if(answer == 3)
  {
    printf("Closest departure time is 12:47 p.m, arriving at 3:00 p.m.");
  }


  return 0;
}
