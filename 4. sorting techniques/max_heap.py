def heapify(arr, i):
    largest = i
    l = left(i)
    r = right(i)
    
    if l < len(arr) and arr[l] > arr[i]:
        largest = l
        
    else:
        largest = i
        
    if r < len(arr) and arr[r] > arr[largest]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, largest)

def left(i):
    return 2 * i + 1

def right(i):
    return 2 * i + 2

# Function to insert an element into the tree
def insert(array, num):
    size = len(array)
    if size == 0:
        array.append(num)
    else:
        array.append(num)
        for i in range((size // 2) - 1, -1, -1):
            heapify(array, i)

arr = []

insert(arr, 12)
insert(arr, 34)
insert(arr, 99)
insert(arr, 22)
insert(arr, 67)
insert(arr, 82)

print ("the max-heap array is: " + str(arr))

def delete_root(arr):
    global n
    lastElement = arr[n - 1] # find last element
    arr[0] = lastElement # replace root element
    n = n - 1 # reduce size of heap by 1
    heapify(arr, 0) # heapify root node
    

def printArray(arr, n):
    for i in range(n):
        print(arr[i],end=" ")
    print()
 
n = len(arr)
delete_root(arr)
printArray(arr, n)

# %%
# Alternate max-heap for array
def max_heap(mylist,i):
    l = left(i)
    r = right(i)
    
    if l < len(mylist) and mylist[l] > mylist[i]:
        largest = l
        
    else:
        largest = i
        
    if r < len(mylist) and mylist[r] > mylist[largest]:
        largest = r
        
    if largest != i:
        mylist[i], mylist[largest] = mylist[largest], mylist[i]
        max_heap(mylist, largest)

def left(i):
    return 2 * i + 1

def right(i):
    return 2 * i + 2

def build_max_heap(mylist):
    n = int((len(mylist)//2)-1)
    for i in range(n, -1, -1):
        max_heap(mylist, i)

def deleteNode(array, num):
    size = len(array)
    i = 0
    for i in range(0, size):
        if num == array[i]:
            break

    array[i], array[size - 1] = array[size - 1], array[i]

    array.remove(size - 1)

    for i in range((len(array) // 2) - 1, -1, -1):
        build_max_heap(mylist)

mylist = [12,34,99,22,67,82]
build_max_heap(mylist)
print(mylist)
