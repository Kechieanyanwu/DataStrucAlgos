# reverse a string using a stack 

def reverse_string(string): #using a stack. Seems like I could've done this with a regular array, but let's still practice
    # convert string into a char[]
    char_array = [char for char in string] # list comprehension. Super useful. Practice more of this when building w Python.l in JS would be string.split('')
    stack = [] # we will interact with the array as a stack, with only pushing and popping methods. Looking at the stack would involve checking out index -1
    for i in range(1, len(char_array) + 1): 
        stack.append(char_array[-i])
    reversed_string = ''.join(stack) # join elements of an array or list into a string 
    return reversed_string
#space complexity - O(n) because it grows proportional to the size of the input -  term is LINEARLY 
#time complexity - O(n) because it grows propotional to the size of the input 

# more concise implementation 
# def reverse_string(string):
#     stack = [char for char in string]
#     reversed_string = ''.join(stack[::-1])
#     return reversed_string

print(reverse_string('gnirts'));

def reverse_stack(stack):
    # stacks seem to relate to recursion. Perhaps because the structure of recursion is a stack itself? 
    # methods for stack are pop, push, peek (looking at index -1), count
    
    # base case is stack is empty
    if len(stack) == 0: # the terminating factor of my recursion
        return 
    
    # pop the stack, store to a variable 
    popped = stack.pop()

    # reverse remaining stack 
    reverse_stack(stack)

    push_to_bottom(stack, popped)

    return stack

def push_to_bottom(stack, element):
    # base case is stack is empty, so push the element
    if len(stack) == 0:
        stack.append(element)
        return

    # take off top of stack
    popped = stack.pop()

    # push the element to the end of the smaller stack 
    push_to_bottom(stack, element)

    #add back the popped element on the reversed stack 
    stack.append(popped)


print(reverse_stack(['g','n', 'i', 'r', 't', 's']))