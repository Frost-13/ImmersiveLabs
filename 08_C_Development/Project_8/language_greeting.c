#include <stdio.h>


int main()
{

#ifdef ENGLISH
printf("Insert Disk 1\n");
#endif

#ifdef FRENCH
printf("Inserez Le Disque 1\n");
#endif

#ifdef SPANISH
printf("Inserte El Disco 1\n");
#endif

return 0;
}