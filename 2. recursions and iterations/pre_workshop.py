# Given an integer, create a function that returns the integer with reversed digits.
# Note: The integer could be either positive or negative.
# test data 
# -231 -> -132
# 345-> 543

# %% -231 -> -132
# Method 1: Polymorphic Reverse Function
def reverse(seq):
    SeqType = type(seq)
    emptySeq = SeqType()
    if seq == emptySeq: 
        return emptySeq
    
    restrev = reverse(seq[1:])
    first = seq[0:1]
    a = restrev + first    
    if seq[0]=='-':
        return f"-{a[:-1]}"   
    else:
        return a

def main():
    print(reverse("-231")) # ans: -132
    
if __name__ == "__main__":
    main()
        
# %% 345 -> 543
# Method 2: Reversing a String
def revString(s):
    if s == "":
        return ""
    
    restrev = revString(s[1:])
    first = s[0:1]
    # Put the pieces together
    result = restrev + first
    
    return result

def main():
    print(revString("345")) # ans: 543
    
if __name__ == "__main__":
    main()
    

# %%
# --------------- SOLUTION --------------- 
def solution(x): 
    string = str(x)
    
    if string[0] == '0':
    # e.g. Hello
    # s[:-3] 
    # output - 'He' 
        return int('-'+string[:0:-1])
    else:
        return int(string[::-1])
    
print(solution(-231))
print(solution(543))

# %%
# Given a string, create a function to find the first non-repeating character in it and return its index. 
# If it doesn't exist, return -1. # Note: all the input strings are already lowercase.
# test data 
# 'alphabet' 1
# 'barbados' 2
# 'crunchy' 1

def FirstNonRepeat(string):
    for i in string:
        if (string.find(i, (string.find(i)+1))) == -1:
            print(i)
            break
    return
 
s = 'alphabet'
letter = FirstNonRepeat(s)
s.find('l') # ans: 1
    
s = 'barbados'
letter = FirstNonRepeat(s)
s.find('r') # ans: 2

s = 'crunchy'
letter = FirstNonRepeat(s)
s.find('r') # ans: 1

# %%
# --------------- SOLUTION --------------- 
def solution(s):
    frequency = {}
    for i in s: 
        if i not in frequency:
            frequency[i] = 1
        else: 
            frequency[i] += 1 
    for i in range(len(s)): 
        if frequency[s[i]] == 1:
            return i
    return -1

print(solution('alphabet'))
print(solution('barbados'))
print(solution('crunchy'))

# # --------------- ALTERNATIVE SOLUTION ---------------  
import collections
def solution(s):
    # build hash map: character and how often it appears
    count = collections.Counter(s) # <- gives back a dictionary with words occurence count
                                   #  # Counter({'l': 1, 'e': 3, 't': 1, 'c': 1, 'o': 1, 'd': 1})
    # find the index
    for idx, ch in enumerate(s):
        if count[ch] == 1:
            return idx
    return -1

print(solution('alphabet'))
print(solution('barbados'))
print(solution('crunchy'))

# %%
def isPalindrome(s):
    reversedString = s[::-1]
    return s == reversedString

def palindromeIf1CharLess(s):
    '''
    Parameters
    ----------
    s : string
        The string will only contain lowercase characters a-z.

    Returns
    -------
    boolean
    you may delete at most one character. Judge whether you can make it a palindrome.

    test data
    ---------
    'radkar'  <- True as it will be a palindrome if you remove d or k
    'apple' <- False
    '''
    if not s:
        return True
    if len(s) <= 2:
        return True
    if isPalindrome(s):
        return True
    i = 0
    j = len(s)-1
    while i < j and s[i] == s[j]:
        i += 1
        j -= 1
    
    if i == j and len(s) % 2 == 1:
        return True
    if i > j and len(s) % 2 == 0:
        return True
    if isPalindrome(s[i:j]): # remove j char
        return True
    if isPalindrome(s[i+1:j+1]): # remove i char
        return True
    return False

palindromeIf1CharLess('radkar')
palindromeIf1CharLess('apple')

# %%
# --------------- SOLUTION --------------- 
# Go through a for loop and check
# The moment you're in the position, join the front and back and then skip i

def palindromeIf1CharLess(s):
    for i in range(len(s)):
        t = s[:i] + s[i+1:]
        if t == t[::-1]: return True
    return s == s[::-1]

s = 'radkar'
print(palindromeIf1CharLess(s))

s = 'apple'
print(palindromeIf1CharLess(s))

# %%
def monotonic(nums): 
    # monotonic: entirely non-increasing or non-decreasing set of ordered values
    '''
    Parameters
    ----------
    nums: an list of integers

    Returns
    -------
    boolean
         nums is monotonic?
    test data
    ---------
        A = [6, 5, 4, 4]  <- True
        B = [1,1,1,3,3,4,3,2,4,2] <- False
        C = [1,1,2,3,7]     <- True
    '''
    x = []
    y = []
    # extending list
    x.extend(nums)
    y.extend(nums)
    x.sort()
    y.sort(reverse=True)
    if(x == nums or y == nums):
        return True
    return False
 
A = [6, 5, 4, 4]
B = [1,1,1,3,3,4,3,2,4,2]
C = [1,1,2,3,7]

# Print required result
monotonic(A) # ans: true
monotonic(B) # ans: false
monotonic(C) # ans: true

# %%
# --------------- SOLUTION --------------- 
# ALL (TRUE, TRUE, TRUE...) = TRUE
# Functional programme will go within the loop to form a tuple
# Goes through a loop for range 
def monotonic(nums):
    return(all(nums[i] <= nums[i+1] for i in range(len(nums)-1)) or 
           all(nums[1] >= nums[i+1] for i in range(len(nums)-1)))

 
A = [6, 5, 4, 4]
B = [1,1,1,3,3,4,3,2,4,2]
C = [1,1,2,3,7]

monotonic(A) 
monotonic(B) 
monotonic(C) 

#%%
# Given an array nums, write a function to move all zeroes to the end of it while maintaining the relative order of 
# the non-zero elements.


def move0sBehind(array, nums):
    '''
    Parameters
    ----------
    nums : list of integer

    Returns
    -------
    nums : list of integer
        move all zeroes to the end of it while maintaining the relative order of the non-zero elements.
    test data
    ---------
        array1 = [0,1,0,3,12]
        array2 = [1,7,0,0,8,0,10,12,0,4]
        
    expected output
    ---------------
        [1, 3, 12, 0, 0]
        [1, 7, 8, 10, 12, 4, 0, 0, 0, 0]
    '''
    for i in range(array.count(0)):
        array.remove(0)
        array.append(0)
         
### ARRAY 1
array1 = [0,1,0,3,12]
nums = len(array1)
move0sBehind(array1, nums)
print(array1) # ans: [1, 3, 12, 0, 0]

### ARRAY 2
array2 = [1,7,0,0,8,0,10,12,0,4]
nums = len(array2)
move0sBehind(array2, nums)
print(array2) # ans: [1, 7, 8, 10, 12, 4, 0, 0, 0, 0]

# %%
# --------------- SOLUTION --------------- 
def move0sBehind(nums):
    for i in nums:
        if 0 in nums:
            nums.remove(0)
            nums.append(0)
        return nums
    
array1 = [0,1,0,3,12]
array2 = [1,7,0,0,8,0,10,12,0,4]
print (move0sBehind(array1))
print (move0sBehind(array2))

#%%
def fillNoneWithPreviousValue(array):
    '''
    Parameters
    ----------
    array : list of string

    Returns
    -------
    res : list of string
        an array containing None values fill in the None values with most recent non None value in the array
    
    test data
    ---------
        array1 = [1,None,2,3,None,None,5,None]
        
    expected output
    ---------------
        [1, 1, 2, 3, 3, 3, 5, 5]
    '''
    # enumerate() adds counter to an iterable and returns it. 
    for i, e in enumerate(array[:-1], 1):
        if array[i] is None:
            array[i] = array[i-1]
    print(array)

array1 = [1,None,2,3,None,None,5,None]
fillNoneWithPreviousValue(array1) # [1, 1, 2, 3, 3, 3, 5, 5]

# %%
# --------------- SOLUTION --------------- 
def fillNoneWithPreviousValue(array):
    valid = 0 
    res = []
    for i in array:
        if i is not None:
            res.append(i)
            valid = i
        else:
            res.append(valid)
    return res

array1 = [1,None,2,3,None,None,5,None]
fillNoneWithPreviousValue(array1) 

#%%
def wordsAppearOnceOnlyIn2Sentence(sentence1, sentence2):
    '''
     Given two sentences, return an array that has the words that appear in one sentence and not
     the other and an array with the words in common. 

    Parameters
    ----------
    sentence1 : string
    sentence2 : string

    Returns
    Returns
    -------
    list of words that appear in either 1 of the sentences
    
    test data
    ---------
        sentence1 = 'We are really pleased to meet you in our city'
        sentence2 = 'The city was hit by a really heavy storm'
        
    expected output
    ---------------
        ['The', 'We', 'a', 'are', 'by', 'heavy', 'hit', 'in', 'meet', 'our', 'pleased', 'storm', 'to', 'was', 'you']
    '''
    # convert string to a list, split by the space character
    sentence1List = sentence1.split(" ")
    sentence2List = sentence2.split(" ")
    
    # set operator before symmetric difference
    sentence1 = set(sentence1List)
    sentence2 = set(sentence2List)

    uncommonwords = sentence2.symmetric_difference(sentence1)
    # return it back into a list
    return list(uncommonwords)

sentence1 = 'We are really pleased to meet you in our city'
sentence2 = 'The city was hit by a really heavy storm'
print(wordsAppearOnceOnlyIn2Sentence(sentence1, sentence2)) 

# %%
# --------------- SOLUTION --------------- 
def wordsAppearOnceOnlyIn2Sentence(sentence1, sentence2):
    set1 = set(sentence1.split())
    set2 = set(sentence2.split())
    
    # ^ = XOR
    return sorted(list(set1^set2)) # ^ A.symmetric_difference(B), & A.intersection(B)

sentence1 = 'We are really pleased to meet you in our city'
sentence2 = 'The city was hit by a really heavy storm'
print(wordsAppearOnceOnlyIn2Sentence(sentence1, sentence2))

#%%
def wordsAppearinBothSentences(sentence1, sentence2):
    '''
          Given two sentences, return an array that has the words that appear in one sentence and not
          the other and an array with the words in common. 

    Parameters
    ----------
    sentence1 : string
    sentence2 : string

    Returns
    -------
    list of words that appear in both sentences
    
    test data
    ---------
        sentence1 = 'We are really pleased to meet you in our city'
        sentence2 = 'The city was hit by a really heavy storm'
        
    expected output
    ---------------
        ['city', 'really']
    '''
    sentence1List = sentence1.split(" ")
    sentence2List = sentence2.split(" ")

    # convert lists to sets and 
    # with '&', gets the 'intersection' (aka the shared words) from both sets
    commonwords = set(sentence1List) & set(sentence2List)

    # return it back into a list
    return list(commonwords) 

sentence1 = 'We are really pleased to meet you in our city'
sentence2 = 'The city was hit by a really heavy storm'
wordsAppearinBothSentences(sentence1, sentence2) # ans: ['city', 'really']

# %%
# --------------- SOLUTION --------------- 
def wordsAppearinBothSentences(sentence1, sentence2):
    set1 = set(sentence1.split())
    set2 = set(sentence2.split())
    
    return sorted(sorted(list(set1&set2)))

sentence1 = 'We are really pleased to meet you in our city'
sentence2 = 'The city was hit by a really heavy storm'
wordsAppearinBothSentences(sentence1, sentence2) # ans: ['city', 'really']

# %%
def primesLessThan(n):
    '''
    Parameters
    ----------
    n : integer.

    Returns
    -------
    prime_nums : list
        the set of prime number less than n
        
    Definition
    ----------
         A prime number is a natural number greater than 1 that has no positive divisors  other than 1 and itself. 
    
    test data
    ---------
        n =35
    expected output
    ---------------
        [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
    '''
    list = []
    for n in range (2, n):  
        if n > 1:  
            for i in range (2, n):  
                if (n % i) == 0:  
                    break  
            else:  
                list.append(n)
    return list

primesLessThan(35)

# %%
# --------------- SOLUTION --------------- 
def primesLessThan(n):
    prime_nums = []
    for num in range(n):
        if num >1: 
            for i in range(2, num):
                if (num % i) == 0: 
                    break
            else:
                prime_nums.append(num)
    return prime_nums

n = 35
primesLessThan(35)        
    