#include <stdio.h>

int gcd(int n, int m)
{
    if(m == 0) //base case :
        return n; //if n % m = 0, n is gcd
    else
        return gcd(m, n % m); 
}
int main(int argc, char **argv)
{
    int n = 54, m = 24;
    printf("gcd of %i and %i = %i\n", n, m, gcd(n, m));
}
