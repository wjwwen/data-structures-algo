# ------ Common Alphabets ------ 
sentence1 = 'We are really pleased to meet you in our city'
sentence2 = 'The city was hit by a really heavy storm'

def CommonAlphabets(sentence1, sentence2):
    # count will contain all the word counts
    common = list(set([c for c in sentence1 if c in sentence2])) 
    print(common)
    
CommonAlphabets(sentence1, sentence2)

# %% 
# ------ Uncommon words ------ 
sentence1 = 'We are really pleased to meet you in our city'
sentence2 = 'The city was hit by a really heavy storm'

def UncommonWords(sentence1, sentence2):
    # count will contain all the word counts
    count = {}
     
    # insert words of string A to hash
    for word in sentence1.split():
        count[word] = count.get(word, 0) + 1
     
    # insert words of string B to hash
    for word in sentence2.split():
        count[word] = count.get(word, 0) + 1
 
    # return required list of words
    return [word for word in count if count[word] == 1]
 
sentence1 = 'We are really pleased to meet you in our city'
sentence2 = 'The city was hit by a really heavy storm'
 
# Print required answer
print(UncommonWords(sentence1, sentence2))

# %%
# ------ Check if the string is a palindrome ------ 
def checkpalindrome(s):
    newS= [i.lower() for i in s if i.isalnum()]
    return newS == newS[::-1]
    
checkpalindrome('radkar')
checkpalindrome('rakar')
checkpalindrome('apple')

# %%
# Reversing numbers
def reverse(x):
    x=str(x)
    if x[0]=='-':
        a=x[::-1]
        return f"{x[0]}{a[:-1]}"
    else:
        return x[::-1]
    
reverse("-231")