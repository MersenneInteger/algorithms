#include <stdio.h>

#define SIZE(x) sizeof(x)/sizeof(x[0])

void selection_sort(int list[], int lo, int hi);
void insertion_sort(int list[], int n);
void bubble_sort(int list[], int sz);

int get_smallest(int list[], int lo, int hi)
{
    for(int i = lo+1; i <= hi; i++)
        if(list[i] < list[lo])
            lo = i;
    return lo;
}

void swap(int list[], int i, int j)
{
    int temp = list[i];
    list[i] = list[j];
    list[j] =  temp;
}
