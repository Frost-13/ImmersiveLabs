#include <stdio.h>
#include <string.h>
#include <stdlib.h>

void quickSortMain(char items[21][21], int count);
void quickSort(char items[21][21], int left, int right);

int main()
{
  int i, count=0, total=0;
  char list[21][21];
  char word[21];
  printf("Enter a word: ");
  fgets(word, 21, stdin);
  while(word[0] != '\n')
  {

    printf("Enter a word: ");
    fgets(word, 21, stdin);

    for(i=0; i<strlen(word); i++)
    {
      list[count][i] = word[i];
    }
    total++;
  }
  quickSortMain(list, total);

  for(i=0; i<total; i++) {
     printf("%s ", list[i]);
  }

  return 0;
}

//######################################################################
void quickSortMain(char items[21][21], int count)
{
  quickSort(items, 0, count);
}

//######################################################################
void quickSort(char items[21][21], int left, int right)
{
  int i, j;
  char *x;
  char temp[21];

  i = left;
  j = right;
  x = items[(left+right)/2];

  do {
    while((strcmp(items[i],x) < 0) && (i < right)) {
       i++;
    }
    while((strcmp(items[j],x) > 0) && (j > left)) {
        j--;
    }
    if(i <= j) {
      strcpy(temp, items[i]);
      strcpy(items[i], items[j]);
      strcpy(items[j], temp);
      i++;
      j--;
   }
  } while(i <= j);

  if(left < j) {
     quickSort(items, left, j);
  }
  if(i < right) {
     quickSort(items, i, right);
  }
  free(x);
}
