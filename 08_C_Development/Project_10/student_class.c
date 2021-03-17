#include <stdio.h>
#include <stdlib.h>

typedef struct {
 int studentID;
 char name[20];
} Student;

int main(){


  Student * p;
  p = (Student *) malloc(2*sizeof(Student));

  Student student1, student2, student3, student4, student5;
  //Student students[10] = {student1, student2, student3, student4, student5};
  int temp=0, count=1;

  while(1){

    //get student ID
    printf("Enter student %d ID: ", count);
    scanf("%d", &p[count].studentID);

    //Check if student ID is -1
    temp = p[count].studentID;
    if(temp == -1){
      break;
    }

    // get student name
    printf("Enter student %d name: ", count);
    scanf("%s", p[count].name);

    //end of list
    if(count == 5){
      printf("You have reached the maximum capacity of the class. You currently have 5 registered students.\n");
      free(p);
      return 0;
    }

    count++;

    // realloc
    if(count == 2){
      p = (Student *) realloc(p, 6*sizeof(Student));
    }


  }
  free(p);
  printf("Thank you. You have %d student(s) in the class.\n", count-1);
  return 0;
}
