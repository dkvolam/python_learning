def add(a,b):
    return a+b
def sub(a,b):
    return a-b
## we can pass function as an argument to another function
def execute(func, a, b,c):
    if c>10:
        x=add(a,b)
    else:
        x=sub(a,b)
    return x   

result=execute('hello', 2, 3,10)
print(result)