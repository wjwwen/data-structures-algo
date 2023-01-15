"""
By: Wang Jing Wen
Matric No: G2101188H

i.	Generate the work files for each .txt
ii.	Combine the work files (remember there may be same items existed in different files) and obtain a sorted file for import into the inventory system.

"""

# %%
# Algorithm 1: You are NOT allowed to use dataframe from pandas
# i. Generate the work files for each .txt
wh1_list = []
wh2_list = []
wh3_list = []
updated_1 = []
updated_2 = []
updated_3 = []

f1 = "WH1.txt"
f2 = "WH2.txt"
f3 = "WH3.txt"

# -------------------------------- (i) Generate file ----------------------------------------
def generatefile_1(f1):
    with open(f1) as fa:
        lines = fa.readlines()
        for line in lines:
            words = line.split(',') # split e.g. A001 and 100
            words = map(lambda s: s.strip(), words) # remove \n characters after values
            for word in words:
                global wh1_list
                wh1_list.append(word)
        updated_1 = [x for x in zip(*[iter(wh1_list)]*2)] # creating list of tuple to get the association between productid and value
        updated_1 = [tuple(int(item) if item.strip().isnumeric() else item for item in group) for group in updated_1]
        
        sums = {}
        for a, b in updated_1:
            if a not in sums: 
                sums[a] = b
            else: 
                sums[a] += b
        mylist = list(sums.items())
        with open('WH1_work.txt','w') as file:
            for l, el in enumerate(mylist):
                string = ','.join(map(str,el)) + '\n'
                for item in string:
                    file.write(item)
            file.write('\n')
            with open('WH1_work.txt') as fa:
                lines = fa.readlines()
                for line in lines:
                    words = line.split(',') # split e.g. A001 and 100
                    words = map(lambda s: s.strip(), words) # remove \n characters after values
                    print(line)


def generatefile_2(f2):
    with open(f2) as fa:
        lines = fa.readlines()
        for line in lines:
            words = line.split(',') # split e.g. A001 and 100
            words = map(lambda s: s.strip(), words) # remove \n characters after values
            for word in words:
                global wh2_list
                wh2_list.append(word)
        updated_2 = [x for x in zip(*[iter(wh2_list)]*2)] # creating list of tuple to get the association between productid and value
        updated_2 = [tuple(int(item) if item.strip().isnumeric() else item for item in group) for group in updated_2]
        
        sums = {}
        for a, b in updated_2:
            if a not in sums: 
                sums[a] = b
            else: 
                sums[a] += b
        mylist = list(sums.items())
        with open('WH2_work.txt','w') as file:
            for l, el in enumerate(mylist):
                string = ','.join(map(str,el)) + '\n'
                for item in string:
                    file.write(item)
            file.write('\n')
            with open('WH2_work.txt') as fa:
                lines = fa.readlines()
                for line in lines:
                    words = line.split(',') # split e.g. A001 and 100
                    words = map(lambda s: s.strip(), words) # remove \n characters after values
                    print(line)
                    
                    
def generatefile_3(f3):
    with open(f3) as fa:
        lines = fa.readlines()
        for line in lines:
            words = line.split(',') # split e.g. A001 and 100
            words = map(lambda s: s.strip(), words) # remove \n characters after values
            for word in words:
                global wh3_list
                wh3_list.append(word)
        updated_3 = [x for x in zip(*[iter(wh3_list)]*2)] # creating list of tuple to get the association between productid and value
        updated_3 = [tuple(int(item) if item.strip().isnumeric() else item for item in group) for group in updated_3]
        
        sums = {}
        for a, b in updated_3:
            if a not in sums: 
                sums[a] = b
            else: 
                sums[a] += b
        mylist = list(sums.items())
        with open('WH3_work.txt','w') as file:
            for l, el in enumerate(mylist):
                string = ','.join(map(str,el)) + '\n'
                for item in string:
                    file.write(item)
            file.write('\n')
            with open('WH3_work.txt') as fa:
                lines = fa.readlines()
                for line in lines:
                    words = line.split(',') # split e.g. A001 and 100
                    words = map(lambda s: s.strip(), words) # remove \n characters after values
                    print(line)

# %%
# -------------------------------- (ii) Combine file ----------------------------------------
original_list = []
updated_list = []
        
def concat_work():
    filenames = ['WH1_work.txt', 'WH2_work.txt', 'WH3_work.txt']
    with open('wh1_wh2_wh3.txt', 'w') as outfile:
        # Iterate through list
        for names in filenames:
                with open(names) as infile:
                   outfile.write(infile.read())
    with open("wh1_wh2_wh3.txt", 'r') as r, open('combinedinput.txt', 'w') as o:
        for line in r:
            #strip() function
            if line.strip():
                o.write(line)
                
    with open("combinedinput.txt") as fa:
        lines = fa.readlines()
        for line in lines:
            words = line.split(',') # split e.g. A001 and 100
            words = map(lambda s: s.strip(), words) # remove \n characters after values
            for word in words:
                global original_list
                original_list.append(word)

        updated_list = [x for x in zip(*[iter(original_list)]*2)]
        updated_list = [tuple(int(item) if item.strip().isnumeric() else item for item in group) for group in updated_list]

        sums = {}
        for a, b in updated_list:
            if a not in sums: 
                sums[a] = b
            else: 
                sums[a] += b
        mylist = list(sums.items())
        
        with open('combinedoutput.txt','w') as file:
            for l, el in enumerate(mylist):
                string = ','.join(map(str,el)) + '\n'
                for item in string:
                    file.write(item)
            file.write('\n')
            with open('combinedoutput.txt') as fa:
                lines = fa.readlines()
                for line in lines:
                    words = line.split(',') # split e.g. A001 and 100
                    words = map(lambda s: s.strip(), words) # remove \n characters after values
                    print(line)


# %%
# Algorithm 2: You MUST use dataframe from pandas
import pandas as pd

def algor2_generate_combine(f1, f2, f3):
    colnames = ['productid', 'quantity']
    df_wh1 = pd.read_csv(f1, sep=",", names=colnames, header=None)
    df_wh1 = df_wh1.groupby('productid').sum()
    # df_wh1.to_csv('WH1_Work_2.txt', index=False, header=None)
    print(df_wh1)

    colnames = ['productid', 'quantity']
    df_wh2 = pd.read_csv(f2, sep=",", names=colnames, header=None)
    df_wh2 = df_wh2.groupby('productid').sum()
    # df_wh2.to_csv('WH2_Work_2.txt', index=False, header=None)
    print(df_wh2)

    colnames = ['productid', 'quantity']
    df_wh3 = pd.read_csv(f3, sep=",", names=colnames, header=None)
    df_wh3 = df_wh3.groupby('productid').sum()
    # df_wh3.to_csv('WH3_Work_2.txt', index=False, header=None)
    print(df_wh3)
    
    df = pd.concat([df_wh1, df_wh2, df_wh3]).groupby(['productid', 'quantity']).sum().reset_index()
    df = df.groupby(["productid"])["quantity"].sum()
    # with open('algor2_combinedoutput.txt', 'w') as file:
    #    df.to_csv(file, header=True, index=False)
    print(df)

# %%
# Algorithm 3:  Must be similar to merge-sort algorithm to compare each record in the file to form the final sorted list.
# Merge Sort
class stocktaking:
    def __init__(self, productid, quantity):
        self.productid = productid
        self.quantity = quantity

    def __str__(self):
        return str.format("productid: {}, quantity: {}", self.productid, self.quantity)

def mergeSort(arr, compare):
    if len(arr) > 1:
        mid = len(arr)//2
        sub_array1 = arr[:mid]
        sub_array2 = arr[mid:]
 
        mergeSort(sub_array1, compare)
        mergeSort(sub_array2, compare)
 
        # pointers to keep track of where we are in each array
        i = j = k = 0
 
        while i < len(sub_array1) and j < len(sub_array2):
            if compare(sub_array1[i], sub_array2[j]):
                arr[k] = sub_array1[i]
                i += 1
            else:
                arr[k] = sub_array2[j]
                j += 1
            k += 1
 
    # When all elements are traversed in either arr1 or arr2,
    # remaining elements put in sorted array
        while i < len(sub_array1):
            arr[k] = sub_array1[i]
            i += 1
            k += 1
 
        while j < len(sub_array2):
            arr[k] = sub_array2[j]
            j += 1
            k += 1
            