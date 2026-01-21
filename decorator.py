# This program gives the demonstration of decoarators in python

# decorators are nothing but functions which 
# 1) take another functions as parameters
# 2) create another function inside the function
# 3) Also return a function from a function

# All the above things are possible because functions are first class objects in python.

# Hiralious definition! Decorators are steroids given to another function to improve the functionality of another function.

# ----------------------------------- DEMO -------------------------------------------

def errorChecker(divisionFunc):

    def inner(a,b):

        # checking if the denominator is zero before dividing
        if(b == 0):
            return "Cannot divide as denominator is 0"
        else:
            return divisionFunc(a,b)
    
    return inner
    

@errorChecker # this line is same as divFunction = errorChecker(divFunc)
def divFunc(a,b):
    return a/b

print(divFunc(10,0))
