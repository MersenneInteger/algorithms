/* Pointer Review */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define SIZE(a) sizeof(a)/sizeof(a[0])

void call_by_ref(int *p)
{
    *p = 7;
}

int _strcmp(char *s, char *t)
{
    while(*s++ == *t++) 
        if(*s == '\0' && *t == '\0')
            return 1;
    return 0;
}

struct student {
    char name[20];
    int id;
};

void make_table(int f, int l, double (*fp)(int))
{
    for(int j = f; j <= l; j++)
        printf("%2d  %0.3f\n", j, (*fp)(j));
}

double reciprocal(int x)
{
    return 1.0/x;
}

double square(int x)
{
    return (x * x);
}

int main(int argc, char **argv)
{
    //basic pointer example
    int n = 5;
    int *p = &n;
    printf("n = %i\n&n = %p\np = %p\n*p = %i\n", n, &n, p, *p);
    
    *p = *p+1;
    printf("*p = %i\n", *p);

    (*p)++;
    printf("*p = %i\n\n", *p);

    // call by reference as opposed to value
    int m = 6;
    printf("m = %i\n", m);
    call_by_ref(&m);
    printf("m = %i\n\n", m);

    //pointer arithmetic
    int a[5] = {0};
    int *pt = a;
    for(int i = 0; i < SIZE(a); i++)
        printf("%i ", *(pt + i));
    printf("\n\n");

    //pointers and strings
    typedef char* string;
    string str = "Love Lain";
    printf("%i\n\n", _strcmp(str, "Love Lain."));

    //generic pointer
    void *gp;
    int o = 7;
    float f = 3.14;
    gp = &o;
    printf("o = %i\n&o = %p\ngp = %p\n*gp = %i\n", o, &o, gp, *(int*)gp);
    gp = &f;
    printf("f = %.2f\n&f = %p\ngp = %p\n*gp = %.2f\n\n", f, &f, gp, *(float*)gp);

    //pointers to structures
    struct student Jake, *Finn;
    strcpy(Jake.name, "Jake");
    Jake.id = 1;
    printf("Name: %s\nId: %i\n", Jake.name, Jake.id);
    
    Finn = &Jake;
    strcpy(Finn->name, "Finn");
    Finn->id = 2;
    printf("Name: %s\nId: %i\n\n", Jake.name, Jake.id);

    //pointers to functions
    void make_table(int, int, double (*fp)(int));
    double reciprocal(int);
    make_table(1,10, reciprocal);
    printf("\n");
    double square(int);
    make_table(1, 10, square);
}
