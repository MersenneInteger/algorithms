#!/usr/bin/env python3
import stack

def balanced_check(s):

    opening_list = ['{', '(', '[']
    closing_list = ['}', ')', ']']

    bracket_stack = stack.Stack()
    for char in s:
        if char in opening_list:
            bracket_stack.push(char)
        elif char in closing_list:
            if bracket_stack.get_size() != 0:
                bracket_stack.pop()
            else:
                return False
    if(bracket_stack.get_size() == 0):
        return True
    return False

#instructor solution
def balanced_check2(s):

    if len(s)%2 != 0:
        return False
        
    opening = set('([{')
    matches = set([('(',')'), ('[',']'), ('{','}')])
    stack_list = []
    for paren in s:
        if paren in opening:
            stack_list.append(paren)
        else:
            if len(stack_list) == 0:
                return False
            else:
                last_open = stack_list.pop()
                if (last_open, paren) not in matches:
                    return False
    return len(stack_list) == 0


print(balanced_check('[]'))
print(balanced_check('[](){([[[]]])}'))
print(balanced_check('()(){]}'))

print(balanced_check2('[]'))
print(balanced_check2('[](){([[[]]])}'))
print(balanced_check2('()(){]}'))