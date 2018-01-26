#include <stdio.h>
#include <stdlib.h>
#include "linked_list.h"

typedef List Stack;

int push(Stack *stack, const void *data);
int pop(Stack *stack, const void **data);
#define peek(stack) ((stack)->head == NULL ? NULL: (stack)->head->data)
#define stack_size list_size

