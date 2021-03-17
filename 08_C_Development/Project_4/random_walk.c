#include <time.h>
#include <stdio.h>
#include <stdlib.h>

void generate_random_walk (int row, int col, char grid[row][col]);
void print_array (int row, int col, char walk[row][col]);


int main(){
int row, col;

printf("insert number of rows: ");
scanf("%d", &row);

printf("insert number of columns: ");
scanf("%d", &col);

char grid[row][col];

int x, y;
for(x=0; x<row; x++){
	for(y=0; y<col; y++){
		grid[x][y] = '.';}
	}
generate_random_walk(row,col,grid);

return 0;
}

void generate_random_walk (int row, int col, char grid[row][col]){

int r,c,rand_num;
int k = 0;
//i = 0;
//j = 0;
r = 0;
c = 0;

char alpha[26] ={'b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'};
grid[0][0]= 'a';
while(k<=25){
// get random int and %4
srand((unsigned)time(NULL));
rand_num = rand()%4;
printf("%d\n", rand_num);	

if(rand_num == 0)
        //i = r;
        //j = c-1;
	c--;
if(rand_num == 1)
       // i = r-1;
       // j = c;
	r--;
if(rand_num == 2)
        //i = r;
        //j = c+1;
	c++;
if(rand_num == 3)
        //i = r+1;
        //j = c;
	r++;
//printf("Char %c, move: %d, col: %d, row: %d, i: %d, j: %d  \n", alpha[k], rand_num, c, r, i, j);

// check to see if it is possible to move to that position. if not break
if(grid[r][c] != '.')
	break;
if(c == col && rand_num == 2)
	break;
if(r == row && rand_num == 3)
	break;
if(r == 0 && rand_num == 1)
	break;
if(c == 0 && rand_num == 0)
	break;
else{       
	grid[r][c] = alpha[k];
        k++;
	//r = i;
	//c = j;
}
}
print_array (row, col, grid);

}

void print_array (int row, int col, char grid[row][col]){

int x,y;
for(x=0; x<row; x++){
        for(y=0; y<col; y++){
               printf("%c", grid[x][y]);}
	printf("\n");}

}
