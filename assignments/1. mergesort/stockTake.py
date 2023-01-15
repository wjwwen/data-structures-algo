"""
By: Wang Jing Wen
Matric No: G2101188H

iii) a python file that import algor.py and perform the entire task name stockTake.py
"""

# %%
from algor import generatefile_1, generatefile_2, generatefile_3
from algor import concat_work
from algor import algor2_generate_combine
from algor import stocktaking, mergeSort


if __name__ == "__main__":
# %%
# --------------------- ALGORITHM 1 ---------------------
    wh1_list = []
    f1 = "WH1.txt"
    generatefile_1(f1)
    
    wh2_list = []
    f2 = "WH2.txt"
    generatefile_2(f2)
    
    wh3_list = []
    f3 = "WH3.txt"
    generatefile_3(f3)
    
    concat_work()

    print("\n")
    print("Output for Algorithm 1:")
    
    print("\n")
    print("(i) Open WH1_work:")
    with open('WH1_work.txt') as f:
        lines = f.readlines()
        print(lines)
    
    print("\n")
    print("(i) Open WH2_work:")
    with open('WH2_work.txt') as f:
        lines = f.readlines()
        print(lines)
    
    print("\n")
    print("(i) Open WH3_work:")
    with open('WH3_work.txt') as f:
        lines = f.readlines()
        print(lines)
        
    print("\n")
    print("(ii) Combined file:")
    with open('combinedoutput.txt') as f:
        lines = f.readlines()
        print(lines)

# %%
# --------------------- ALGORITHM 2 ---------------------
    print("\n")
    print("Output for Algorithm 2:")
    # Algor2: Combine and Generate WH1_work, WH2_work, WH3_work
    
    algor2_generate_combine(f1, f2, f3)

# %%    
# --------------------- ALGORITHM 3 ---------------------
    print("\n")
    print("Output for Algorithm 3:")
    # Algor3: Combine and Generate WH1_work, WH2_work, WH3_work
    st1 = stocktaking('A001', 100)
    st2 = stocktaking('B010', 600)
    st3 = stocktaking('C022', 200)
    st4 = stocktaking('D011', 520)
    st5 = stocktaking('A003', 300)
    st6 = stocktaking('B004', 200)
    st6 = stocktaking('C006', 600)
    st7 = stocktaking('D008', 800)
    
    st8 = stocktaking('B004', 100)
    st9 = stocktaking('C005', 200)
    st10 = stocktaking('A003', 22)
    st11 = stocktaking('B007', 300)
    st12 = stocktaking('D008', 900)
    st13 = stocktaking('B004', 600)
    st14 = stocktaking('B010', 800)
    
    st15 = stocktaking('A001', 10)
    st16 = stocktaking('A001', 200)
    st17 = stocktaking('C022', 12)
    st18 = stocktaking('C022', 20)
    st19 = stocktaking('A003', 300)
    st20 = stocktaking('B004', 200)
    st21 = stocktaking('C006', 600)
    st22 = stocktaking('D008', 800)
    
    arr1 = [st1,st2,st3,st4,st5,st6,st7]
    arr2 = [st8, st9, st10, st11, st12, st13, st14]
    arr3 = [st15, st16, st17, st18, st19, st20, st21, st22]
    arr = arr1+arr2+arr3
    
    mergeSort(arr, lambda prod1, prod2: prod1.productid < prod2.productid)
    print("Products sorted by projectid:")
    for p in arr:
        print(p)
        
    print("\n")
