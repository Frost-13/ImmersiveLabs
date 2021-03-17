# include <stdio.h>
int main()
{   int dollar;
    printf("Enter a dollar amount: ");
    scanf("%d", &dollar);
    
    int twnt = dollar / 20;
    int temp_dol = dollar - (twnt*20);

    int ten = temp_dol  / 10;
    temp_dol = temp_dol - (ten*10);

    int five = temp_dol / 5;
    temp_dol = temp_dol - (five *5);

    int one = temp_dol;

    printf("$20 bills: %d \n", twnt);
    printf("$10 bills: %d \n", ten);
    printf("$5 bills: %d \n", five);
    printf("$1 bills: %d \n", one);
    return 0;
}    
