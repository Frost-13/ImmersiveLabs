#include<stdio.h>
#include<stdlib.h>
#include<string.h>


//save global variables for the mapping file. the letters and their respective numbers
int  map_nums[26];
char letters[26];


void encrypt(char inputText[], int inputLength, int key);
void decrypt(int cipherText[], int inputLength, int key);

int main(int argc, char*argv[])
{

// declaring all variables in main()
char word[100];
int  numbers[20];
int  mode, key, i, j;
char * map_name;
FILE *map_f;
FILE *input_f;

if(argc!=9)
{
        fprintf(stderr,"Usage: ./encrypt -t <mappingfile> -k <secret key> -m <encryption mode> -i <inputfile>\n");
	return 8;
}


// going through all the flags and assigning variables respectivly
for(i=1; i<argc; i++)
{
        if(strcmp(argv[i], "-t") == 0)
        {
                // Reading Mapping File
		map_name = argv[i+1];
                map_f =  fopen(map_name, "r");
                i++;

                if (map_f == NULL)
                {       /*can't open file*/
                        fprintf(stderr, "ERROR: mapping file  %s does not exist.\n", argv[i]);
                        return 3;
                }
         }

       else if(strcmp(argv[i], "-i") == 0)
        {
                input_f =  fopen(argv[i+1], "r");
                i++;

                if (input_f == NULL)
                {       /*can't open file*/
                        fprintf(stderr, "ERROR: input word file %s does not exist.\n",argv[i] );
                        return 5;
                }
         }

       else if(strcmp(argv[i], "-k") == 0)
        {
                key = atoi(argv[i+1]);
                i++;
                if(key<0 || key>25)
                {
                        fprintf(stderr, "you entered %d . sorry your key must be between 1 and 25. Re-run the program and try again\n", key);
                        return 6;
                }
        }

        else if(strcmp(argv[i], "-m") == 0)
        {
                mode = atoi(argv[i+1]);
                i++;
                if(mode< 1 || mode>  2)
                {
                        fprintf(stderr, "You entered %d. Sorry, your mode must be 1 for encryption or 2 for decryption\n", mode);
                        return 7;
                }
        }
	
	else
	{
	        fprintf(stderr, "Usage: ./encrypt -t <mappingfile> -k <secret key> -m <encryption mode> -i <inputfile>\n");
       	 	return 8;
	}
}


// make 2 arrays one with alphabet and the other with the coorespoinding number
j = 0;
while(j<=25)
{
        char let;
	int num;

        fscanf(map_f, "%c,%d\n", &let, &num);
        	
	map_nums[j] = num;
	letters[j] = let;
	j++;
}


// if encryption mode is chosen  
if(mode == 1)
{
        while(fgets(word, 100, input_f))
                if(!feof(input_f))
                        encrypt(word, strlen(word), key);
}

// if decryption mode is chosen
if(mode == 2)
{

	int i=0, count=0, num=0;
	char letter;
       	while(!feof(input_f))
	{
		if(fscanf(input_f, "%d", &num))
        	{
			numbers[i] = num;
			i++;
			count++;
		}
		else
		{	
			if(fscanf(input_f, "%c", &letter))
			{
                        decrypt(numbers, count, key);
			count = 0;
			j=0;
			}
		}
	}
}
//close files
fclose(input_f);
fclose(map_f);

return 0;
}



// this is where i made new functions***********************************************
void encrypt(char inputText[], int inputLength, int key)
{
        int k =0;
        int num;
        int j = inputLength-2;

        // go through the line of input file backwards
        // goes through the alphabet and checksto see if which charachter it is
        // once it gets a match it takes the cooresponded mapping value
        // and does the math needed to encrypt 
        while(j>=0)
        {
                k = 0;
                while(k<=25)
                {
                        if(letters[k] ==inputText[j])
                        {
                                num = map_nums[k];
                                num -= key;
                                num += 26;

                               fprintf(stdout,"%d ", num);
                        }
                        k++;
                }

                j--;
        }
fprintf(stdout,"\n");
return;
}




void decrypt(int cipherText[], int inputLength, int key)
{
        //initiate variables
        int k =0;
        int num;
        int j = inputLength-1;
 
        while(j>= 0)
        {     
                num = cipherText[j];
                num += key;
               

                if(num>26)
                {
                        num = num-26;
                 
                }
                
                k = 0;
                while(k<=25)
                {
                        if(map_nums[k] == num)
                        {
                                fprintf(stdout,"%c", letters[k]);
                        }
                        k++;
                }

                j--;
        }
fprintf(stdout,"\n");
return;
}

