'''ZeroDivisionError
ValueError
TypeError
KeyError
IndexError
FileNotFoundError
NameError
The are the error names in python. We can handle these errors using try except block. 
We can also use finally block to execute some code regardless of whether an exception is raised or not.
we have to give names exactly like these in exception block to handle the specific error. 
If we want to handle all the errors we can use Exception as e in except block.
'''

try:
    a=int(input('enter any number'))
    print(10/a)
except ZeroDivisionError:
     print('you cannot divide by zero')
except TypeError:
    print("you should enter a valid type")
except ValueError:
    print("you should enter a number")