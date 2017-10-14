/* selection sort: O(n^2) */
#include <stdio.h>
#include "sort.h"

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
void selection_sort(int list[], int lo, int hi)
{
    for(int i = lo; i < hi; i++){
        for(int j = 0; j <= hi; j++)
            printf("%i ", list[j]);
        printf("\n");
        int s = get_smallest(list, i, hi);
        swap(list, i, s);
    }
}

int main(int argc, char **argv)
{
    int list[] = {6, 9, 2, 5, 8, 3, 4};
    selection_sort(list, 0, SIZE(list)-1);
    printf("\n");
    for(int i = 0; i < SIZE(list); i++)
        printf("%i ", list[i]);
    
}
