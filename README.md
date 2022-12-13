# Week 1: Principles of Algorithmic Design
> Algorithm: Correctness and Performance <br>
An algorithm may not be a program.

## Computational complexity
1. Time complexity
2. Space complexity

Primitive: Integer, Float, String, Boolean
Non-primitive: Array, List, Tuple, Dictionary, Set, File

## Application Memory 
Heap > Stack > Static/Global > Code

## == v.s. is
The == operator compares the value or equality of two objects, whereas the Python is operator checks whether two variables point to the same object in memory.

## Estimating the efficiency of algorithm 
- Post-implementation **profiling** approach: let it run with live data and choose the best candidate
- Pre-implementation **theoretical** aprroach: approximated mathematically before running algorithm

## XOR
```python
# (a and not b) or (not a and b)
# bool(a) ^ bool(b)
def logical_xor(str1, str2):
    return bool(str1) ^ bool(str2)
```

# Big O Notation
> Big O notation is used to measure the performance of any algorithm by providing the order of growth of the function
It gives the **upper bound** on a function by which we can make sure that the function will never grow faster than this upper bound
We want the **approximate** runtime of the operations performed on data structures.

If f(n) and g(n) are two functions,
f(n) = 0(g(n))

If there exists constants c and n0 such that
f(n) <= c.g(n), for all n >= n0

> This simply means that f(n) does not grow faster than g(n).
Providing growth rate of the function, which eventually gives the worst case time complexity...

![Common Data Structure Operations](https://external-preview.redd.it/_s_OgE9SF3fuWLLr5fY0-ZC2RmKfC6hgztbpXgslhNc.png?auto=webp&s=61991a48130b90b50df9925b4da29f2502080619)

# Course Outline
2. Recursions and Iterations
3. Sorting Techniques
4. Searching Techniques
5. Abstract Data Type
6. Linear Data Structure
7. Hierarchical Data Structure
8. Network Data Structure
9. Java/Javascript/Full stack w Nodejs
10. Aynchronous v.s. Synchronous Programming
11. Concurrency and Parallelism
12. Summary

# Week 2: Iterations and Recursions
- Functions revisit
- Iterative functions
- Recursive functions

```python
def computeGST(amount, includedGST, gstPercent=0.07):
    if includedGST:
    gst = amount/(1+gstPercent) * gstPercent
    amtb4 = amount – gst
    total = amount
else:
    gst = amount * gstPercent
    amtb4 = amount
    total = amtb4 + gst
return amtb4, gst, total 
```

## How to use *args in Python
- *args: pass a variable number of non-keyword arguments to a Python function
- **kwargs: pass a variable number of keyword arguments to a Python function

### *args
```python
def total_fruits(**kwargs):
    print(kwargs, type(kwargs))
```

### output:
```python
{'banana':5, 'mango':7, 'apple':8} <class:'dict'>
```

### **kwargs
```python
def total_fruits(**fruits):
    total = 0 
    for amount in fruits.values():
        total += amount
    return total

print(total_fruits(banana=5, mango=7, apple=8))
print(total_fruits(banana=5, mango=7, apple=8, oranges=10))
print(total_fruits(banana=5, mango=7)
```

## Iterations
- For...
- While...

## Recursion
- A problem is expressed in a similar form to the original problem but smaller in scope
- Useful for divide and conquer problems

### Factorial n! = n*(n-1)*(n-2)*...*1
- The base case when n is zero
- The recursive case when n is greater than zero

```python
def factorial(n):
# test for a base case
    if n==0:
        return 1
    else:
    # make a calculation and a recursive call
    f = n*factorial(n-1)
    print(f)
    return(f)

factorial(4) 
```

| Recursion                                                         | Iteration                                   |
| -----------                                                       | -----------                                 |
| Terminates when a base case is reached                            | Terminates when a defined condition is met  |
| Requires space in memory                                          | Not stored in memory                        |
| An infinite recursion results in a stack overflow error           | An infinite iteration will run while the hardware is powered                                                             | 
| Some problems are naturally better suited to recursive solutions  | Iterative solutions may not always be obvious       |

> Tail end recursion: when there is 1 recursive call in the algorithm and this call is the very last thing the method does <br>
e.g. reverseList, nothing is passed and return to the previous calls

### When should we **NOT** use recursion?
- The algo/data structure is not naturally suited for recursive calls
- The recursive function is long and hard to understand the coding
- The time taken using recursive call is too long to be accepted in a practical situation
- Too much space (memory) is used
- Too many repeated computations

## Divide and Conquer Algorithm
- Many useful algos are recursive in structure, i.e., to solve the given problem, they call themselves recursively one or more times to deal with closely related sub-problems


| Divide and Conquer                                                | Dynamic Programming                         |
| -----------                                                       | -----------                                 |
| Divide: into a smaller subproblem; Conquer: Solving sub-problem recursively; Combine: solution of the sub-problem to find a final solution                                                      | Characterizing the structure of an optimal solution; Define value of an optimal solution recursively; bottom-up algorithm, calculate value of an optimal solution; Using computed information, construct optimal solution           |
| Recursive                                                         | Non-recursive                                         |
| Recursively works on sub-problem, consumes more time              | Solves sub-problem only once, consumes less time      |
| Top-down algorithm                                                | Bottom-up algorithm                                   |
| Sub-problems are independent by nature                            | Sub-problems are interdependent in nature                                                              |
| e.g. Linear search and Merge sort                                 | e.g. Matrix multiplication                            |

## Timeit v.s. CProfiler
- timeit module: useful for measuring small code snippets
- cProfile module: more effective for analyzing entire functions or programs. 
Profiling analyzes your program’s speed, memory usage, and other aspects systematically. Measure a program’s runtime as well as build a profile of runtimes for the program’s individual function calls. This information provides substantially more granular measurements of your code.

| ncalls      | tottime    | percall    | cumtime    | percall    | filename:lineno(function) |
| ----------- | ---------- | ---------- | ---------- | ---------- | ----------                | 
| no. of calls made to the function  | total time spent in the function, excl time in sub functions  | total time divided by no. of calls | cumulative time spent in the functions and subfunctions | cumulative time divided by the no. of calls | the file the function is in and at which line no.

## Higher Order Functions
> If it contains other functions as a parameter/returns a function as an output
- Functions as objects
- Passing Function as an argument to other function
- Returning function
- Decorators
- Reverse Decorators

# Week 3: Searching Algorithms
## Data Structures in Python
- List 
```python
x = [2,3,5,11]
```
- Tuple
```python
Q1=('Jan', 'Feb', 'Mar', 'Apr')
```
- Set
```python
s=set()
```
- Dict

## Linear Search
- Disadvantage: Very slow due to exhaustive search
- Advantage: Data does not need to be sorted

## Binary Search
- O(logN)

## Hashing
> Using an array for the efficient storage/retrieval of information.
The technique behind hashing is to enable, as far as possible, storage and retrieval of data in a constant average time of approximately **O(1)**.

Using an array for retrieval of data:

| Linear Search      | Binary Search    | Only when Index known    | 
| -----------        | ----------       | ----------               | 
| O(n)               | O(log2n)         | O(1)                     | 

Using an array for storage of data:

| Unsorted           | Sorted      |  
| -----------        | ----------  | 
| O(1)               | O(n)        | 

### Ideal Hashing Table
- One-to-one mapping of keys (keys onto integers)

Store: <br>
```python
for each item key ki loop 
    evaluate h = H(ki)
    if slot h in table empty then
        store item in slot h 
    else
        examine successive slots
        store item in first empty slot end
    end
end
````

Locate: <br>
```python
evaluate h = H(ki) 
while slot h not empty
        and key not found loop 
    try next slot
end loop
if slot h empty then
    item not in table 
end if
```

# Week 4: Bubble Sort
Insertion Sort (pseudo code)
```python
InsertionSort (List : array of items)
For I = 1 to N loop
    itemToInsert = List[I] //copy of next item to be inserted
    indexHole = I //index of hole where item to be inserted was
    //locate where to insert the item within the sorted part of the list
    While indexHole > 0 and List[indexHole-1] > itemToInsert loop
        List[indexHole] = List[indexHole-1]
        indexHole = indexHole-1
    end while
// located place to insert the item within sorted list
    List[indexHole] = itemToInsert
end loop
end InsertionSort
```

Selection Sort (pseudo code)
```python
SelectionSort(List : array of items)
    Set N = number of items in the List
    for I =1 to N -1
        Set indexSmallest = I
        for J= I+1 to n //find index of smallest item in the unsorted part of the list
            if List[J]< List[indexSmallest]then
                indexSmallest = J
        endif
        endloop
        if indexSmallest ≠ I then //index smallest located, move item to position I
        swap (List[indexSmallest], List[I])
        endif
    endloop
end SelectionSort
```
## Min and Max Heap Operations
### Minimum Heap Operations
- A Min-Heap is a complete binary tree in which the value in each internal node is smaller than or equal to the values in the children of that node

### Maximum Heap Operations
- Taking the bigger number
- Able to sort by descending order for Linked List

## Heap Data Structure
- heapq
- min heap: smallest of heap element is popped 
- quick sort > heap sort

## Merge Sort
1. Recursively sort the left half of the input array
2. Recursively sort the right half of the inpt array
3. Merge two sorted sub arrays into one

```python
# Python program for implementation of MergeSort
def mergeSort(arr):
    if len(arr) > 1:
 
         # Finding the mid of the array
        mid = len(arr)//2
 
        # Dividing the array elements
        L = arr[:mid]
 
        # into 2 halves
        R = arr[mid:]
 
        # Sorting the first half
        mergeSort(L)
 
        # Sorting the second half
        mergeSort(R)
 
        i = j = k = 0
 
        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
 
        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
 
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
 
# Code to print the list
 
 
def printList(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()
 
 
# Driver Code
if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6, 7]
    print("Given array is", end="\n")
    printList(arr)
    mergeSort(arr)
    print("Sorted array is: ", end="\n")
    printList(arr)

```

# Week 5: Linear Data Structures
Abstract Data Type (ADT): interface to which the data structure must adhere

| ADT                                             | Data Structure                          |
| -----------                                     | -----------                             |
| High level description                          | Concrete description                    |
| Concerned with what it can do                   | Concerned with how a task is done       |
| Implementation independent                      | Implementation dependent                |

# Week 6: Graph Data Structure
Node = Vertex
Graphs can be classified into 4:
1. Undirected graphs
2. Directed graphs
3. Undirected multigraphs
4. Directed multigraphs

## Understanding Graph Traversals
1. Breadth-first search (BFS)
2. Depth-first search (DFS)

