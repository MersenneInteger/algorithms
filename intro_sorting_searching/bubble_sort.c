/* bubble sort: O(n^2) */

#include <stdio.h>
#include "sort.h"

void bubble_sort(int list[], int sz)
{
    for(int i = 1; i < sz; i++)
        for(int j = 0; j < sz; j++)
            if(list[i] < list[j])
                swap(list, i, j);
}
int main(int argc, char **argv)
{
    int list[] = {6, 2, 5, 9, 3};
    for(int i = 0; i < SIZE(list); i++)
        printf("%i ", list[i]);
    printf("\n");
    bubble_sort(list, SIZE(list));
    for(int i = 0; i < SIZE(list); i++)
        printf("%i ", list[i]);
    printf("\n");
}
