# Singly and Doubly Linked Lists
**Singly Linked List**: set of nodes where each node has two fields ‘data’ and ‘link’. The ‘data’ field stores actual piece of information and ‘link’ field is used to point to next node. Basically the ‘link’ field stores the address of the next node.

**Doubly Linked List**: contains an extra pointer, typically called previous pointer, together with next pointer and data which are there in singly linked list. 


| Singly                                                        | Doubly |
| -----------                                                   | ----------- |
| 1 direction                                                   | Both directions (backward and forward)         |
| Less memory as it stores in 1 address                         | More memory as it stores in two address        |
| Complexity of insertion/deletion at a known position is O(n)  | Complexity of insertion/deletion at a known position is O(1)       |

![Singly and Doubly](https://res.cloudinary.com/practicaldev/image/fetch/s--QTk9XbRm--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://thepracticaldev.s3.amazonaws.com/i/kvnpce96zqdxu73hp6oe.png)