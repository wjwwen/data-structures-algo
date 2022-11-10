# Week 1: Principles of Algorithmic Design
> Algorithm: Correctness and Performance <br>
An algorithm may not be a program.

# Computational complexity
1. Time complexity
2. Space complexity

Primitive: Integer, Float, String, Boolean
Non-primitive: Array, List, Tuple, Dictionary, Set, File

# Application Memory 
Heap > Stack > Static/Global > Code

# == v.s. is
The == operator compares the value or equality of two objects, whereas the Python is operator checks whether two variables point to the same object in memory.

# Estimating the efficiency of algorithm 
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
2. Iterations and Recursions
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