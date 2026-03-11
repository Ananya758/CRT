'''
Bug--> Error
finding and fixing of errors is called debugging.
Types of errors:-
1. Syntax errors --> Missing of colons, missing of identation
2. Runtime errors --> Division any num by 0
3. Logical errors --> missing of logics
Debugging Techniques:-
1. print() --> run the code line by line.
2. try - except
3. using of pdb --> pdb(Python Debugger)
                    Purpose:- 
                    1. Pass the flow of execution
                    2. inspect the variable's value
                    3. too run the code step by step
                    pdb commands:-
                    1. n --> to get output in nextline
                    2. p variable --> to get the value of that variable
                    3. l --> list nearby code
                    4. c --> continue the execution
                    5. s --> start the function
                    6. r --> to return from the function
                    7. h --> help
                    8. q --> quit the execution
'''
'''
a = int(input("Enter a:"))
b = int(input("Enter b:"))
c = a + b
print("value of a:", a)
print("value of b:", b)
print("sum of c:", c)


try:
    a = int(input("Enter a:"))
    print(10/a)
except ZeroDivisionError:
    print("Can not divisible by zero")
except ValueError:
    print("Invalid input")
'''


import pdb
def add(a, b):
    pdb.set_trace()
    return a + b
a = int(input("Enter a:"))
b = int(input("Enter b:"))
print(add(a, b))
