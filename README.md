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

1. Divide: Break the problem into several sub-problems that are similar to the original problem but smaller,
2. Conquer: Solve the sub-problem recursively, and if the sub-problem sizes are small enough, just straightforwardly solve the sub-problems
3. Combine: Combine this solution to create a solution to the original problem

| Divide and Conquer                                                | Dynamic Programming                         |
| -----------                                                       | -----------                                 |
| Divide: Dividing the original problem into a smaller subproblem; Conquer: Solving sub-problem recursively; Combine: Combine the solution of the sub-problem to find a final solution                                                      | Characterizing the structure of an optimal solution; Define the value of an optimal solution recursively; Using the bottom-up algorithm, calculate the value of an optimal solution; Using computed information, construct an optimal solution           |
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
