a=10
def hello():
    global a
    a+=5
    print('Hello,am a', a)
print('Hello,am a', a)
print('boundary')
hello()
print('i changed the global variable a')
print(a)