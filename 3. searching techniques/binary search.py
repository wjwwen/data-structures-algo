# -*- coding: utf-8 -*-
"""

The pseduo code of the Binary Search is as follows:
    
"""

'''
Java : iterative
public class BinarySearch {

 public int binarySearchIteratively(int[] sortedArray, int key) {
  int low = 0;
     int high = sortedArray.length - 1;
  int index = Integer.MAX_VALUE;

  while (low <= high) {

   int mid = (low + high) / 2;

   if (sortedArray[mid] < key) {
    low = mid + 1;
   } else if (sortedArray[mid] > key) {
    high = mid - 1;
   } else if (sortedArray[mid] == key) {
    index = mid;
    break;
   }
  }
  return index;
 }
'''

def BinarySearch(mylist, item): 
   low = 0 
   high = len(mylist)-1 
   index = -1
   while low<=high :         
        mid = (high + low)//2    
        if mylist[mid] < item:                 
                low = mid+1             
        elif mylist[mid] > item:                    
                high = mid-1        
        else:
            index = mid
            break
   return index


mylist = [11,22,33,45,80,88]   # must  be sorted already
print(mylist)
print("finding 23:", BinarySearch(mylist,23))
print("finding 33:", BinarySearch(mylist,33))

#%%
'''
Java : recursive
 public int binarySearchRecursively(int[] sortedArray, int key, int low, int high) {

  int middle = (low + high) / 2;
  if (high < low) {
   return -1;
  }

  if (key == sortedArray[middle]) {
   return middle;
  } else if (key < sortedArray[middle]) {
   return binarySearchRecursively(sortedArray, key, low, middle - 1);
  } else {
   return binarySearchRecursively(sortedArray, key, middle + 1, high);
  }
 }

 
 public static void main(String[] args) {
  int[] sortedArray = { 0, 1, 2, 3, 4, 5, 5, 6, 7, 8, 9, 9 };
     int key = 6;
     
     BinarySearch binSearch = new BinarySearch();
        
        int index = binSearch.binarySearchRecursively(sortedArray, key, 0, sortedArray.length -1);
        System.out.println("Search element found in location index : " + index);
        
 }
}
'''
def BinarySearchR(mylist, item, low, high): 
    middle = (low + high)//2  
    if high < low:
        return -1
    if item==mylist[middle]:
        return middle
    elif item < mylist[middle]:
        return BinarySearchR(mylist,item,low,middle-1)
    else:
        return BinarySearchR(mylist,item,middle+1, high)


mylist = [11,22,33,45,30,88]   # must  be sorted already
print(mylist)
print("finding 23:", BinarySearchR(mylist,23,0, len(mylist)-1))
print("finding 33:", BinarySearchR(mylist,33,0, len(mylist)-1))