#include <stdio.h>
#include <stdlib.h>
int main(int arg, char *argv[]){

// read the file and save the date
FILE* fp = fopen(argv[1], "r");

if (fp == NULL){/*can't open file*/
	fprintf(stderr, "ERROR: input.txt doesn't.\n");
	exit(EXIT_FAILURE);
	}

int f_month;
int f_day;
int f_year;

fscanf(fp, "%d/%d/%d", &f_month, &f_day, &f_year);

fclose(fp);
// get the user date
int month;
int day;
int year;
printf("Enter date to compare to (mm/dd/yy): ");
scanf("%d/%d/%d", &month, &day, &year);

// chechks to make sure he dates are valid
if ((f_month==1 || f_month==3 || f_month==5 || f_month==7 || f_month==8 || f_month==10 || f_month==12) &&(f_day > 31)){ 
	fprintf(stderr,"Wrong date format\n");
	exit(4);
	}
if ((month==1 || month==3 || month==5 || month==7 || month==8 || month==10 || month==12) && (day > 31)){
        fprintf(stderr,"Wrong date format\n");
	exit(4);
	}

if ((f_month==4 || f_month==6 || f_month==9 || f_month==11) && (f_day > 30)){
        fprintf(stderr,"Wrong date format\n");
	exit(4);
	}
if ((month==4 || month==6 || month==9 || month==11) && (day > 30)){
        fprintf(stderr,"Wrong date format\n");
	exit(4);
	}
if ((f_month==2) && (f_day > 28)){
	fprintf(stderr,"Wrong date format\n");
	exit(4);
	}
if ((month==2) && (day > 28)){
        fprintf(stderr,"Wrong date format\n");
	exit(4);
	}
if (f_year>18|| f_year<0|| year>18|| year<0|| f_month>12|| f_month<1|| month>12|| month<1){
        fprintf(stderr,"Wrong date format\n");
        exit(4);
        }
// compare the two dates
else if (f_year < year)
        printf("\n%d/%d/%.2d is earlier than %d/%d/%.2d\n", f_month , f_day, f_year, month, day, year);

else if (f_month < month)
        printf("\n%d/%d/%.2d is earlier than %d/%d/%.2d\n", f_month , f_day, f_year, month, day, year);

else if (f_day < day)
        printf("\n%d/%d/%.2d is earlier than %d/%d/%.2d\n", f_month , f_day, f_year, month, day, year);

else
        printf("\n%d/%d/%.2d is later than %d/%d/%.2d\n", f_month , f_day, f_year, month, day, year);
// doesnt put the 0 in the years for example 8 instead of 08 
return 0;
}
