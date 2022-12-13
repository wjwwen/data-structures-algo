# ------------------ 1. Reverse Stack ------------------
# Function to display the contents of the stack S
def display(S):
    # Iterate while S is not empty
    while len(S) > 0:
        # Print the top element of the stack S
        print(S[-1], end = " ")
        # Pop from S
        S.pop()
    print()
 
# Function to reverse a stack using two stacks
def reverseStackUsingTwoStacks(S):
    # Two additional stacks
    A = []
    B = []
    # Transfer all elements from the stack S to A
    while len(S) > 0:
        A.append(S[-1])
        S.pop()
    # Transfer all elements from the stack A to B
    while len(A) > 0:
        B.append(A[-1])
        A.pop()
    # Transfer all elements from the stack B to S
    while len(B) > 0:
        S.append(B[-1])
        B.pop()
    # Print the contents of S
    display(S)
 
# Given Input
S = []
S.append(5)
S.append(4)
S.append(3)
S.append(2)
S.append(1)
 
# Function call
reverseStackUsingTwoStacks(S)

# %%
# Python program to demonstrate stack implementation using list
s1 = []
# append() function to push
# element in the stack
s1.append('a')
s1.append('b')
s1.append('c')
print('Initial stack') 
print(s1)

# pop() function to pop
# element from stack in
# LIFO order
print('\nElements popped from stack:') 
print(s1.pop())
print(s1.pop())
print(s1.pop())
print('\nStack after elements are popped:')
print(s1)

# uncommenting print(stack.pop()) # will cause an IndexError
# as the stack is now empty