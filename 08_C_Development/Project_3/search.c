# include <stdio.h>
# include <stdlib.h>
int main(int argc, char *argv[]){

int thresh = atoi(argv[2]);
int i, j =0;
FILE*fp =  fopen(argv[1], "r");

if (fp == NULL){/*can't open file*/
        fprintf(stderr, "ERROR: input.txt doesn't.\n");
        exit(EXIT_FAILURE);
        }
char word[100];
char let[26] = {'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'};

int num[26] ={0};// {'0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'};


while(fgets(word, 100, fp)){
	//printf("%s", word);
	i = 0;
	while(word[i] != '\n'){
		//printf("%c\n", word[i]);
		i++;
		for(j=0; j<26; j++){
			if(word[i] == let[j]){
				num[j]++;
				//printf("%d", num[j]);
				//printf("%s\n", "works");
				}
			}
		}				
}
i = 0;
//printf("%a", let)
for(i=0; i<26; i++){
	if((num[i] != 0) && (num[i] > thresh)){
		printf("%c appears %d times\n", let[i], num[i]);  
	}
}
fclose(fp);
return 0;
}
