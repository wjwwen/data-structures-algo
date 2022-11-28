# Linked List
Singly Linked List: 
Each element in a linked list is called a node. A single node contains data and a pointer to the next node which helps in maintaining the structure of the list.

![Singly](https://media.geeksforgeeks.org/wp-content/cdn-uploads/gq/2013/03/Linkedlist.png)

Doubly Linked List: contains an extra pointer, typically called the previous pointer, together with the next pointer and data which are there in the singly linked list.

![Doubly](https://media.geeksforgeeks.org/wp-content/cdn-uploads/gq/2014/03/DLL1.png)

> Time Complexity: O(n)

| Singly                                        | Doubly                                                                |
| -------------------                           | -------------------                                                   |
| 2 fields - data field and next link field.    | 3 fields - data field, a previous link field, a next link field       |
| Unidirectional                                | Bidirectional                                                         |
| Occupies less memory                          | Occupies more memory                                                  |
| Complexity = O(n)                             | Complexity = O(n)                                                     |
| Execute stacks                                | Execute heaps and stacks, binary trees                                |
| Better for non-searching operations           | Better for search operations                                          |

# Stack
LIFO (Last-In-First-Out) principle
Allows insertion and deletion operations from one ned of the stack data structure

![Stack](https://cdn.programiz.com/sites/tutorial2program/files/stack-operations.png)

> Time Complexity: O(1)

# Array
A collection of items stored at contiguous memory locations. The idea is to store multiple items of the same type together. This makes it easier to calculate the position of each element by simply adding an offset to a base value, i.e., the memory location of the first element of the array (generally denoted by the name of the array).

![Array](https://www.guru99.com/images/1/102319_0559_ArrayinData2.png)

# Tree
> Time Complexity: O(log(n))

A Tree data structure is used to store hierarchical data (it is non-linear), 
such as an Operating System file system.

A Tree contains "nodes" (a node has a value associated with it) and each node is 
connected by a line called an "edge". These lines represent the relationship 
between the nodes.

The top level node is known as the "root" and a node with no children is a "leaf".

If a node is connected to other nodes, then the preceeding node is referred to 
as the "parent" and nodes following it are "child" nodes.

## Binary Trees

There is a specific type of tree referred to as a "Binary Tree", which restricts 
its child nodes to no more than two.

The children of a node are referred to as the "left" node and the "right" node.

When creating a Binary Tree object you'll pass in the first node to become the 
root node and each node is itself an object with an associated value, along with 
a left and right node linked to.

## Binary Search Trees

There is another type of tree called a "Binary Search Tree" and this is an 
extension of the Binary Tree, with the addition that the child nodes are stored 
in a specific order depending on a custom calculation.

The calculation is very simple: if a node has a lesser value than its parent it 
is placed in the "left" node position. If on the other hand it has a greater value 
than its parent it is placed in the "right" node position.


### Usefulness

- Quick to search
- Quick insertion/deletion

# Hashmap/Hashtable
> A hash table organizes data so you can quickly look up values for a given key.
Hashmaps are built on arrays.
- https://www.interviewcake.com/concept/java/hash-map

|        | Average   | Worst Case   |
| ------ | --------- | ------------ |
| Space  |   O(n)    |    O(n)      |
| Insert |   O(1)    |    O(n)      |
| Lookup |   O(1)    |    O(n)      |
| Delete |   O(1)    |    O(n)      |

Java has two hash table classes: HashTable and HashMap. In general, you should use a HashMap.

| HashTable                           | Hashmap                                                    |
| ---------                           | ------------                                               |
|  Does not allow null keys/values    |    Allows null keys/values                                 |
|  Synchronised to prevent multiple threads from accessing it at once    |    Not synchronised     |