# %%
# SELECTION SORT

# Time Complexity = O(n*n)

# Sorting by finding min_index
def selectionSort(array, size):
    for ind in range(size):
        min_index = ind
 
        for j in range(ind + 1, size):
            # select the minimum element in every iteration
            if array[j] < array[min_index]:
                min_index = j
         # swapping the elements to sort the array
        (array[ind], array[min_index]) = (array[min_index], array[ind])
 
arr = [12, 33, 11, 45, 87, 30]
size = len(arr)
selectionSort(arr, size)
print('The array after sorting in Ascending Order by selection sort is:')
print(arr)


# %%
# Using lambda function
q = sorted([('Ali', 165), ('Charles', 220), ('Bala', 338), ('Diana', 523)], key = lambda x:x[1])
print(q)

# %%
# Iterative tools
from more_itertools import sort_together
SalesPerson = ['Ali', 'Bala', 'Charles', 'Diana']
SalesQty = [165, 338, 220, 523]

q = sort_together([SalesPerson, SalesQty], key_list=[1])
print(q)
print(SalesPerson)
print(SalesQty)

# %%
# Sort by key/values
dic = {2.90, 1: 100, 8: 3, 5: 67, 3: 5}
dic2 = dict(sorted(dic.items(), key = lambda x:x[0]))
print(dic2)
