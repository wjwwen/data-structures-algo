# Function to heapify the tree
def heapify(arr, n, i):
    # Find the largest among root, left child and right child
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[i] < arr[l]:
        largest = l

    if r < n and arr[largest] < arr[r]:
        largest = r

    # Swap and continue heapifying if root is not largest
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


# Function to insert an element into the tree
def insert(array, newNum):
    size = len(array)
    if size == 0:
        array.append(newNum)
    else:
        array.append(newNum)
        for i in range((size // 2) - 1, -1, -1):
            heapify(array, size, i)

arr = []

insert(arr, 12)
insert(arr, 34)
insert(arr, 99)
insert(arr, 22)
insert(arr, 67)
insert(arr, 82)

print ("Max-Heap array: " + str(arr))

# Function to delete an element from the tree
def deleteRoot(arr):
    global n
 
    # Get the last element
    lastElement = arr[n - 1]
 
    # Replace root with last element
    arr[0] = lastElement
 
    # Decrease size of heap by 1
    n = n - 1
 
    # heapify the root node
    heapify(arr, n, 0)
    
# A utility function to print array of size n
def printArray(arr, n):
 
    for i in range(n):
        print(arr[i],end=" ")
    print()
 
n = len(arr)
 
deleteRoot(arr)
 
printArray(arr, n)