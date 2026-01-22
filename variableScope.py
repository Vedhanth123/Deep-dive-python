
# There are 4 types of variables in python
# LEGB
# L -> Local (written inside a function and used inside a function)
# E -> Enclosing (written inside outside a function but inside a parent function)
# G -> Global (written at the top of the file)
# B -> Built in (default python variables)

# global variable
salary = 100

role = "joker"

def changeSalary():

    # enclosed
    stipend = 10

    if(role == 'joker'):

        def jokerSalaryChange():
            
            # local variable 
            money = 1

            # to change the global variable you have to use `global` keyword
            global salary
            salary *= 0.2


        