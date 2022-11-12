#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A recursive function is simply a function that calls itself.
Every recursive function must have a base case (to prevent stack overflow)
"""

# %%
# Sum of Integers
def sumFirstN(n):
    return n * (n+1) // 2

def main():
    x = int(input("Please enter a non-negative integer: "))
    
    s = sumFirstN(x)
    
    print("The sum of the first", x, "integers is", str(s)+".")
    
if __name__ == "__main__":
    main()
    
# %%
# Recursive Sum of Integers
def recSumFirstN(n):
  if n == 0:
      return 0
  else:
      return recSumFirstN(n-1) + n
 
def main():
  x = int(input("Please enter a non-negative integer: "))

  s = recSumFirstN(x)

  print("The sum of the first", x, "integers is", str(s)+".")

if __name__ == "__main__":
  main()
  
# %%
# No Else Needed
def recSumFirstN(n):
  if n == 0:
      return 0

  return recSumFirstN(n-1) + n

# %%
# List Recursion
def revList(lst):
    accumulator = []
    
    for x in lst:
        accumulator = [x] + accumulator
        
def main():
    print(revList([1,2,3,4]))
    
if __name__ == "__main__":
    main()

# %%
# Version 1: Reversing a List
def revList(lst):
    # Here is the base case
    if lst == []:
        return []
    
    # The rest of this function is the recursive case.
    # This works because we called it on something smaller.
    # The lst[1:] is a slice of all but the first item in lst.
    restrev = revList(lst[1:])
    first = lst[0:1]
    
    # Now put the pieces together
    result = restrev + first
    
    return result

def main():
    print(revList([1,2,3,4]))
    
if __name__ == "__main__":
    main()

# %%
# Version 2: Reversing a list 
def revList2(lst):
    def revListHelper(index):
        if index == -1:
            return []
        
        restrev = revListHelper(index-1)
        first = [lst[index]]
        
        # Now put the pieces together
        result = first + restrev
        
        return result
    # this is the one line of code for the revList2 function
    return revListHelper(len(lst)-1)

def main():
    print(revList2([1,2,3,4]))

if __name__ == "__main__":
    main()

# %%
def revString(s):
    if s == "":
        return ""
    
    restrev = revString(s[1:])
    first = s[0:1]
    # Now put the pieces together
    result = restrev + first
    
    return result

def main():
    print(revString("hello"))
    
if __name__ == "__main__":
    main()

# %%
"""
Reflection = code to be able to examine attributes about objects
that may be passed as parameters to a function

e.g. See what the type of an object is
"""

# Polymorphic reverse function: work to reverse any sequence
# Polymorphic: evaluate/be applied to values of different types
# Polymorphic due to reflection and operator overloading

# Reflection Reverse
def reverse(seq):
    SeqType = type(seq)
    emptySeq = SeqType()
    if seq == emptySeq: 
        return emptySeq
    
    restrev = reverse(seq[1:])
    first = seq[0:1]
    
    # Now put the pieces together
    result = restrev + first
    return result

def main():
    print(reverse([1,2,3,4]))
    print(reverse("hello"))
    
if __name__ == "__main__":
    main()
    