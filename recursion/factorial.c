#include <stdio.h>

long long iter_fact(int n)
{
    long long p = 1;
    for(int i = 1; i <= n; i++)
        p *= i;
    return p;
}

long long recu_fact(long long n)
{
    if(n == 1)
        return n;
    else
        return n * recu_fact(n-1);
}

long long tail_fact(long long n, long long a)
{
    if(n == 1)
        return a;
    else
        return tail_fact(n-1, n*a);
}

int main(int argc, char **argv)
{
    printf("iterative factorial\n");
    printf("%lli\n", iter_fact(5));
    printf("recursive factorial\n");
    printf("%lli\n", recu_fact(5));
    printf("tail recursive factorial\n");
    printf("%lli \n", tail_fact(5, 1));
}
