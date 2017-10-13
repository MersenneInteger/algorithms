#include <stdio.h>

void iter_fib(int upbnd)
{
    long long first = 0, second = 1, sum;
    for(int i = 0; i < upbnd; i++){
        sum = first + second;
        first = second;
        second = sum;
        printf("%lli ", sum);
    }
}

void recu_fib(long long f, long long s, int upbnd)
{
    if(upbnd == 0)
        return;
    else {
        printf("%lli ", f + s);
        recu_fib(s, f + s, --upbnd);
    }
}

long long nth_fib(int n)
{
    static long long first = 0, second = 1, sum;
    if(n == 0)
        return second;
    else {
        sum = first + second;
        first = second;
        second = sum;
        nth_fib(--n);
    }
}

int main(int argc, char **argv)
{
    printf("iterative fibonacci\n");
    iter_fib(10);
    printf("\nrecursive fibonacci\n");
    recu_fib(0, 1, 10);
    printf("\nnth fibonacci\n");
    printf("%lli \n", nth_fib(7));
}
