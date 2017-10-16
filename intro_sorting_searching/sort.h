#include <stdio.h>

#define SIZE(x) sizeof(x)/sizeof(x[0])

void selection_sort(int list[], int lo, int hi);
void insertion_sort(int list[], int n);
void bubble_sort(int list[], int sz);
void string_sort(int lo, int hi, int max, char list[][max]);
int binary_search(int lo, int hi, int list[], int key);
int bsearch(int lo, int hi, int list[], int key);

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

void insert(int n, int list[], int lo, int hi)
{
    int k = hi;
    while(k >= lo && n < list[k]){
        list[k+1] = list[k];
        --k;
    }
    list[k+1] = n;
}
