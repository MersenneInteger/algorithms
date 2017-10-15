/* selection sort: O(n^2) */
#include <stdio.h>
#include "sort.h"

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
