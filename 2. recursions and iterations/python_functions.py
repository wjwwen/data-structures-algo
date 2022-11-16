# %% 
# --------------- FIBONACCI NUMBERS (DYNAMIC PROGRAMMING) -------------------

memo = [] 
memo.append(0) 
memo.append(1) 

def fibonacciVal(n):
    if n <len(memo): 
        return(memo[n])
    else:
        for i in range(len(memo), n+1):
            memo.append( memo[i-1] + memo[i-2])
    return memo[n]
for i in range(1,35): 
    print(fibonacciVal(i))

# %% 
# ----------------------- FUNCTION AS OBJECTS -----------------------

 # Python program to illustrate functions can be treated as objects
def shout(text):
    return text.upper() 
print(shout('Hello'))

# Assigning function to a variable yell = shout
yell = shout
print(yell('Hello'))

# %%
#  ----------------------- PASSING FUNCTION -----------------------
def shout(text):
    return text.upper()

def whisper(text):
    return text.lower()

def greet(func):
    # storing the function in a variable
    greeting = func("Hi, I am created by a function passed as an argument")
    print(greeting)

greet(shout)
greet(whisper)

# %%
#  ----------------------- RETURNING FUNCTION -----------------------
def create_adder(x):
    def adder(y):
        return x + y
    return adder

add_15 = create_adder(15)

print(add_15(10))

# %%
#  ----------------------- DECORATOR -----------------------
def hello_decorator(func):
    # inner1 = Wrapper function, calling argument
    # inner function can access the outer local functions like in this case "func"
    def inner1():
        print("Hello, this is before function execution")
        # calling the actual function now inside the wrapper function
        print("This is after function execution") 
    return inner1

# defining a function, to be called inside wrapper 
def function_to_be_used():
    print("This is inside the function !!")
# passing 'function_to_be_used' inside the decorator to control its behavior
function_to_be_used = hello_decorator(function_to_be_used)
function_to_be_used()

# %%
# ----------------------- DECORATOR -----------------------
def hello_decorator(func): # *****
        def inner1():
            print("Hello, this is before function execution")
            func()
            print("This is after function decorator")
        return inner1

@hello_decorator
def function_to_be_used():
    print("This is inside the function!")
    return None

function_to_be_used()

# %%
# ----------------------- REVERSE DECORATOR -----------------------
def reverse_decorator(function):
    def reverse_wrapper():
        make_reverse = "".join(reversed(function()))
        return make_reverse
    return reverse_wrapper

@reverse_decorator
def say_hi():
    return 'Hi George'

def main():
    print(say_hi())

if __name__ == "__main__": 
    main()
    
    