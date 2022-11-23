'''
Linear Search
'''


'''
Java:
        public static int linerSearch(int[] arr, int key){
         
        int size = arr.length;
        for(int i=0;i<size;i++){
            if(arr[i] == key){
                return i;
            }
        }
        return -1;
    }
'''

def LinearSearch(inlist, item):      
    for i in range(len(inlist)):
        if inlist[i] == item:             
            return i      
    return -1


mylist = [12,33,11,45,87,30]
print(mylist)
print("finding 23:", LinearSearch(mylist,23))
print("finding 33:", LinearSearch(mylist,33))

#%%
''' Another way to write with while
'''
def LinearSearch(list, item):     
    index = 0     
    found = False 
# Match the value with each data element     
    while index < len(list) and found is False:         
        if list[index] == item:             
            found = True         
        else:             
            index = index + 1     
    return found


mylist = [12,33,11,45,87,30]
print(mylist)
print("finding 23:", LinearSearch(mylist,23))
print("finding 33:", LinearSearch(mylist,33))