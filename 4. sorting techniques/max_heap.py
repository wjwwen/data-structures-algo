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
