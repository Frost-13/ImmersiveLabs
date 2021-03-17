#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>
#include "puzzle2D.h"


int main(int argc, char*argv[])
{
FILE *puz_f;
FILE *word_f;
char puzzle[1001][1001];
char temp[1001];
int end;

// varialbes for output.txt
FILE* out_f;
char out_name[10001] = "output.txt";


// goes through all the flags and handles errors accordingly and sets variables accordingly
if(argc!=5 && argc!=7)
{
        fprintf(stderr,"Usage: ./wordSearch2D -p <puzzle_file> -w <wordlist_file> [-o <solution_file>]\n");
	return 6;
}


// going through all the flags and assigning variables respectivly
for(int i=1; i<argc; i++)
{
        if(strcmp(argv[i], "-p") == 0)
        {
                // Reading Puzzle File
                puz_f =  fopen(argv[i+1], "r");
                i++;
		
                if (puz_f == NULL)
                {       // can't open file
                        fprintf(stderr, "ERROR: puzzle file  %s does not exist.\n", argv[i]);
                        return 4;
                }
			
         }

       else if(strcmp(argv[i], "-w") == 0)
        {
                word_f =  fopen(argv[i+1], "r");
                i++;

                if (word_f == NULL)
                {       // can't open file
                        fprintf(stderr, "ERROR: Wordlist file %s does not exist.\n",argv[i] );
                        return 5;
                }
         }


       else if(strcmp(argv[i], "-o") == 0)
        {
                strncpy(out_name, argv[i+1], strlen(argv[i+1]));
                i++;
	    }
       else
       {
            fprintf(stderr,"Usage: ./wordSearch2D -p <puzzle_file> -w <wordlist_file> [-o <solution_file>]\n");
	        return 6;
       }       
}
//puts(out_name);

//create output file
out_f =  fopen(out_name, "w");

	// go through puzzle file and make a 2d array of the puzzle
    int i =0, size=0;
    while(fgets(temp, 1001, puz_f))
    {
        end = strlen(temp)-1;
        if(!feof(puz_f))
        {
            for(int j=0; j<strlen(temp)-1; j++)
            {
		
				//check if acii value
				int ascii = temp[j];
				if(ascii<32 || ascii>126)
				{
					fprintf(stderr, "Encountered error");
        			return 7;
				}
				puzzle[i][j] = temp[j];
        		//printf("%c", puzzle[i][j]);
        	}
            size++;
            i++;
        	//printf("\n");
        }
    }

    
	//if not n by n
    if(size != end)
    {
        fprintf(stderr, "Encountered error");
        return 7;
    }
    
    char *p;
    char word[1001];
    long solution;
    // go through the word file line by line 
    	while(fgets(word, 1001, word_f))
                    if(!feof(word_f))
                    {
                        p = strchr(word, '\n');
                        if( p != NULL)
                            *p ='\0';
						
						//check for no ascii values
						for(i = 0; i<strlen(word); i++)
						{
							int ascii = word[i];
								if(ascii<32 || ascii>126)
								{
									fprintf(stderr, "Encountered error");
        							return 7;
								}
                        }
                        // call a function that takes that 1 line and the whole puzzle file
			// call each one until we find the word
                        //puts(word);
                        solution = hash(word);
                        if(horizontal_forward(word, puzzle, size, solution, out_f))
                            continue;                              
                        else if(horizontal_back(word, puzzle, size, solution, out_f))
                            continue; 
                        
                        else if(vertical_up(word, puzzle, size, solution, out_f))
                            continue;

                        else if(vertical_down(word, puzzle, size, solution, out_f))
                            continue;

                        else if(diagonal_down_right(word, puzzle, size, solution, out_f))
                            continue;
                        
                        else if(diagonal_down_left(word, puzzle, size, solution, out_f))
                            continue;

                        else if(diagonal_up_right(word, puzzle, size, solution, out_f))
                            continue;

                        else if(diagonal_up_left(word, puzzle, size, solution, out_f))
                            continue;
                        // if we dont find the word
                        else
                            fprintf(out_f, "%s;(0,0);0\n", word);                        
                            
                    }
	
	//close files
    fclose(out_f);
    fclose(puz_f);
    fclose(word_f);
    
    return 0;
    }
