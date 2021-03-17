#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>
#include "puzzle2D.h"

#define p 101


// reads the maze from left to right
// all 8 functions have the same structure so i will just comment this function
int horizontal_forward(char word[], char puzzle[1001][1001], int size, long solution, FILE *f)
{ 
    //initialize variable
    int length = strlen(word);
    char temp[length];
	int j, count;

	//read through al the rows in the puzzle
	for (int row= 0; row<=size-1; row++)
	    {
			// read through all the columns 
			for (int col=0; col<=(size-1)-(length-1); col++)
            {	
    			j=col;
				//save the word and hash it to check to see if it is the solution and if it is print
				//it to the file and leave this fuction and move on to the next word
				for (count =0; count<=(length-1); count++)
				{ 
                    temp[count]= puzzle[row][j++]; 
                }
                temp[count] = '\0';
                if(solution == hash(temp))
                {
                    fprintf(f,"%s;(%d,%d);1\n", word, row, col);
                    return 1;
                }				
                //printf("%s\n", temp);

			}
		}
	return 0;
}

// reads the maze from right to left
int horizontal_back(char word[], char puzzle[1001][1001], int size, long solution, FILE *f)
{
    int length = strlen(word);
    char temp[length];
    int j, count;
	for (int row= 0; row<=size-1; row++)
	{
	    for (int col=size-1; col>=(length-1); col--)
        {
		    j=col;
			for (count =0; count<=(length-1); count++)
			{
                temp[count]= puzzle[row][j--];
            }
             temp[count] = '\0';
             if(solution == hash(temp))
             {
                fprintf(f,"%s;(%d,%d);2\n", word, row, col);
                return 1;
             }
			//printf("%s\n", temp);

		}
	}
	return 0;
}


// reads maze from top to bottom
int vertical_down(char word[], char puzzle[1001][1001], int size, long solution, FILE *f)
{
    int length = strlen(word);
    char temp[length];
	int i, count;
	for (int row= 0; row<=(size-1)-(length-1); row++)
	{
	    for (int col=0; col<=(size-1); col++)
		{
    		i=row;
			for (count =0; count<=(length-1); count++)
			{
                temp[count]= puzzle[i++][col];
            }
            temp[count] = '\0';
            if(solution == hash(temp))
            {
                fprintf(f,"%s;(%d,%d);3\n", word, row, col);
                return 1;
            }    		
    		//	printf("%s\n", temp);
            
        }
	}
	return 0;
}

// reads maze from bottom to top
int vertical_up(char word[], char puzzle[1001][1001], int size, long solution, FILE *f)
{
    int length = strlen(word);
    char temp[length];
	int i, count;
    for (int row= size-1; row>=(length-1); row--)
    	{
    		for (int col=0; col<=size-1; col++)
			{
    			i=row;
				for (count =0; count<=(length-1); count++)
                {
                    temp[count]= puzzle[i--][col];
                }
                temp[count] = '\0';
				if(solution == hash(temp))
                {
                    fprintf(f,"%s;(%d,%d);4\n", word, row, col);
                    return 1;
                }

			}
		}
	return 0;
}

// reads maze from top left to bottom right
int diagonal_down_right(char word[], char puzzle[1001][1001], int size, long solution, FILE *f)
{
	int length = strlen(word);
	//printf("%d", length);
	char temp[length];
	int i, j, count;
	for(int row =0; row<=(size-1)-(length-1); row++)
		{
			
		    for (int col=0; col<=(size-1)-(length-1); col++)
				{ 
                    i=row;
				    j=col;

					for(count =0; count<=length-1; count++)
						{
							temp[count] = puzzle[i++][j++];
						}
                        temp[count] = '\0';
					    if(solution == hash(temp))
                        {
                            fprintf(f,"%s;(%d,%d);5\n", word, row, col);
                            return 1;
                        }
					//printf("%s\n",temp);
				}
         }
    return 0;
}

// reads maze from top right to bottom left
int diagonal_down_left(char word[], char puzzle[1001][1001], int size, long solution, FILE *f)
{
	int length = strlen(word);
	//printf("%d", length);
	char temp[length];
	int i, j, count;
	for(int row =0; row<=(size-1)-(length-1); row++)
		{
			for (int col=size; col>=(length-1); col--)
				{   
                    i=row;
                    j=col;
					
                    for(count =0; count<=length-1; count++)
						{
							temp[count] = puzzle[i++][j--];
                        }
                        temp[count] = '\0';
					    if(solution == hash(temp))
                        {
                            fprintf(f,"%s;(%d,%d);8\n", word, row, col);
                            return 1;
                        }
				}
         }
    return 0;
}

// reads maze from bottom left to top right
int diagonal_up_right(char word[], char puzzle[1001][1001], int size, long solution, FILE *f)
{
	int length = strlen(word);
	//printf("%d", length);
	char temp[length];
	int i, j, count;
	for(int row =size-1; row>=(length-1); row--)
		{
			for (int col=0; col<=(size-1)-(length-1); col++)
				{ 
                    i=row;
				    j=col;

				for(count =0; count<=length-1; count++)
					{
						temp[count] = puzzle[i--][j++];
					}
                     temp[count] = '\0';
					 if(solution == hash(temp))
                     {
                        fprintf(f,"%s;(%d,%d);7\n", word, row, col);
                        return 1;
                     }
					//printf("%s\n",temp);
				}
         }
    return 0;
}

//reads maze from bottom right to top left
int diagonal_up_left(char word[], char puzzle[1001][1001], int size, long solution, FILE *f)
{
	int length = strlen(word);
	//printf("%d", length);
	char temp[length+1];
	int i, j, count;
	for(int row =size-1; row>=(length-1); row--)
		{
			for (int col=size-1; col>=(length-1); col--)
				{ 
                    i=row;
                    j=col;

				for(count=0; count<=length-1; count++)
					{
						temp[count] = puzzle[i--][j--];
					}
                    temp[count] = '\0';
					if(solution == hash(temp))
                    {
                        fprintf(f,"%s;(%d,%d);6\n", word, row, col);
                        return 1;
                    }
					//printf("%s\n",temp);
				}
         }
    return 0;
}


//finds the hash value using the Rabin-Karp algorithm
long hash(char word[1001])
{
    //printf("%s\n", word);
    //printf("last char: %c\n", word[2]);
    long length= strlen(word);
    //printf("length: %d\n", length);
    long total=0, temp, count = length-1;

    for(int i =0; i<=length-1; i++)
    {
        temp = word[i];
        temp = temp*(pow(p, count)); 
        total += temp;
        count--;
    }
    //printf("%ld\n", total);
    return total;
}
