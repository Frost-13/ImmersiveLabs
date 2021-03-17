#include <stdio.h>

int gcd(int m, int n)
{

    if(n == 0)
		return m;
    else
        return gcd(n, m%n);
}

int main()
{
	int m, n;
    printf("Enter two intigers: ");
	scanf("%d%d", &m, &n);
	
    int answ;
	answ = gcd(m, n); 

    printf("greatest common divisor: %d\n", answ);

    return 0;
}