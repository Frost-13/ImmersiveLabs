#include <stdio.h>

void avg_sum(double a[], int n, double *avg, double *sum);

int main()
{
        double a[10] = {4, 5, 6, 8.5, 9, 3, 2, 10, 4, 19};

        double sum, average;

        avg_sum(a, 10, &average,&sum);

        printf("The sum is = %.2lf and the avg = %.2lf\n",sum, average);

        return 0;
}

void avg_sum(double a[], int n, double *avg, double *sum)
{
        *sum = 0.0;

        for(int i = 0; i < n; i++)
        {
                *sum += a[i];

                *avg = *sum/ n;
        }
return;
}

