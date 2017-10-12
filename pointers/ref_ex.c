#include <stdio.h>
#include <string.h>
#include <stdlib.h>

typedef char* string;
void swap_by_val(int x, int y)
{
    int temp = y;
    y = x;
    x = temp;
}

void swap_by_ref(int *x, int *y)
{
    int temp = *y;
    *y = *x;
    *x = temp;
}

string reverse(string s)
{
    string dest = malloc(sizeof(s));
    int len = strlen(s)-1;
    for(int i = len; i >= 0; i--)
        *(dest + (len-i)) = *(s+i);
    return dest;
}

int main(int argc, char **argv)
{
    int n = 3, m = 5;
    printf("n = %i\nm = %i\n", n, m);
    swap_by_val(n, m);
    printf("swap by value: n = %i\nm = %i\n", n, m);

    printf("n = %i\nm = %i\n", n, m);
    swap_by_ref(&n, &m);
    printf("swap by reference: n = %i\nm = %i\n\n", n, m);

    //reverse a string with pointers
    string str = "abcde";
    printf("str = %s\nreversed = %s\n", str, reverse(str));
}
