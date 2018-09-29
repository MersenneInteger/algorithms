#include <stdio.h>
#include <stdlib.h>
#include "stack_list.h"

int push(Stack *stack, const void *data)
{
    return insert_next(stack, NULL, data);
}

int pop(Stack *stack, const void **data)
{
    return remove_next(stack, NULL, data);
}

int main(int argc, char **argv)
{
    Stack stack;
    int *data;
    
    init_stack(&stack, free);
    push(&stack, (int*)5);
    push(&stack, (int*)3);
    for(int i = 0; i < stack_size(&stack); i++)
        printf("%i ",(int*)peek(stack));
}
