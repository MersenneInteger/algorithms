#include <stdio.h>
#include <stdlib.h>

#define SIZE 10

typedef struct {
    int top;
    int stack_array[SIZE];
} *Stack, Stack_Type;

Stack init()
{
    Stack S = malloc(sizeof(Stack_Type));
    S->top = -1;
    return S;
}
int push(int elem, Stack S)
{
    if(S->top < SIZE-1) {
        ++(S->top);
        S->stack_array[S->top] = elem;
        return 1;
    } else
        printf("Stack full");
    return 0;
}

int pop(Stack S)
{
    if(S->top != -1){
        --(S->top);
        return S->stack_array[S->top];
    } else
        printf("Stack empty");
    return 0;
}

int peek(Stack S)
{
    if(S->top != -1)
        return S->stack_array[S->top];
    else
        printf("Stack empty");
    return 0;
}

void print_stack(Stack S)
{
    for(int i = 0; i <= S->top; i++)
        printf("%i\n", S->stack_array[i]);
}
int main(int argc, char **argv)
{
    Stack stack = init(stack);
    push(3, stack);
    push(5, stack);
    print_stack(stack);
    printf("popping...");
    pop(stack);
    print_stack(stack);
    push(8, stack);
    push(4, stack);
    printf("peek = %i\n\n", peek(stack));
    print_stack(stack); 
}
