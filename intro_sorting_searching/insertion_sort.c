/* insertion sort: O(n^2) */

#include <stdio.h>
#include "sort.h"

void insertion_sort(int list[], int n)
{
    int key, j;
    for(int i = 1; i < n; i++) {
        key = list[i];
        j = i-1;
        while(j >= 0 && key < list[j]) {
            list[j+1] = list[j];
            --j;
        }
        list[j+1] = key;
        for(int k = 0; k < n; k++)
            printf("%i ", list[k]);
        printf("\n");
    }
}

int main(int argc, char **argv)
{
    int list[] = {6,2,5,3,9,8,1};
    insertion_sort(list, SIZE(list));
} 
