# %%
# Implementation of Node
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
    def __repr__(self):
        return self.data
    
# %%
class LinkedList:
    def __init__(self):
        self.head = None # nonexisting list
    
    def search(self, item): 
        node = self.head 
        while node is not None:
            if node.data == item:
                return node 
            node = node.next 
        return None
    
    # Iterate through the nodes and print nodes
    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)
    
    # Testing
    if __name__ == "__main__":
        llist = LinkedList()
        print(llist)
        new_node = Node("A")
        llist.head = new_node
        print(llist)
        print(llist.search('A'))
        print(llist.search('B'))
        
        new_node = Node("b")
        new_node.next = llist.head
        llist.head = new_node
        print(llist)
        print(llist.search('A'))
        print(llist.search('B'))
    
# Stack as a subclass
class Stack(LinkedList):
    def push(self, new_node):
        new_node.next = self.head
        self.head = new_node
    def pop(self):
        popNode = self.head
        self.head = self.head.next
        return popNode
    
if __name__ == "__main__":
    s = Stack()
    print(s)
    n = Node("a")
    s.push(n)
    print(s)
    
    n = Node("b")
    s.push(n)
    print(s)
    print(s.pop())
    print(s)
    
    n = Node("c")
    s.push(n)
    print(s)
    
    n = Node("d")
    s.push(n)
    print(s)
    print(s.pop())
    print(s.pop())
    print(s)

