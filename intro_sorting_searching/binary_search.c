#include <stdio.h>
#include "sort.h"

int binary_search(int lo, int hi, int list[], int key)
{
    int mid;
    while(lo <= hi) {
        mid = (lo + hi) / 2;
        if(key == list[mid])
            return mid;
        if(key < list[mid])
            hi = mid-1;
        else
            lo = mid + 1;
    }
    return -1;
}

//binary search using recursion
int bsearch(int lo, int hi, int list[], int key)
{
    int mid = (lo + hi)/2;
    if(key == list[mid])
        return mid;
    if(key < list[mid])
        bsearch(lo, mid-1, list, key);
    else if(key > list[mid])
        bsearch(mid+1, hi, list, key);
    else
        return -1;
}

int main()
{
    int primes[] = {2,3,5,7,11,13,17,19,23,29};
    int n = binary_search(0, SIZE(primes), primes, 3);
    if(n != -1)
        printf("Found at [%i]\n", n);
    n = bsearch(0, SIZE(primes), primes, 5);
    if(n != -1)
        printf("Found at [%i]\n", n);
}
