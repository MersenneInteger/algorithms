#include <stdio.h>
#include <string.h>
#include "sort.h"

#define N 4
#define M 10

void string_sort(int lo, int hi, int max, char list[][max])
{
    char key[max];
    for(int i = lo+1; i <= hi; i++) {
        strcpy(key, list[i]);
        int k = i-1;
        while(k >= lo && strcmp(key, list[k]) < 0){
            strcpy(list[k+1], list[k]);
            --k;
        }
        strcpy(list[k+1], key);
    }
}

void parallel_sort(int lo, int hi, int max, char list[][max], int num[])
{
    char key[max];
    for(int i = lo+1; i <= hi; i++) {
        strcpy(key, list[i]);
        int m = num[i];
        int k = i-1;
        while(k >= lo && strcmp(key, list[k]) < 0){
            strcpy(list[k+1], list[k]);
            num[k+1] = num[k];
            --k;
        }
        strcpy(list[k+1], key);
        num[k+1] = m;
    }
}
int main(int argc, char **argv)
{
    char list[N][M] = {"cat", "bat", "rat", "ant"};
    for(int i = 0; i < SIZE(list); i++)
        printf("%s ", list[i]);
    string_sort(0,N-1,M,list);
    printf("\n");
    for(int i = 0; i < SIZE(list); i++)
        printf("%s ", list[i]);
    printf("\n\n");

    char nlist[N][M] = {"cat", "bat", "rat", "ant"};
    int legs[N] = {4, 2, 4, 8};
    for(int i = 0; i < SIZE(nlist); i++)
        printf("%s : %i legs\n", nlist[i], legs[i]);
    parallel_sort(0,N-1,M,nlist,legs);
    printf("\n");
    for(int i = 0; i < SIZE(nlist); i++)
        printf("%s : %i legs\n", nlist[i], legs[i]);
    
}
