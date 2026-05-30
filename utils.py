# #print('running from utils module')
# def add(a, b):
#     return a + b

# if __name__ == '__main__':
#     print('Any developer who want to use this module, explicityly call add method')
#     #print('2 + 3 =', add(2, 3))

# print(__name__)

def add(a, b):
    return a + b

print("utils name:", __name__)

if __name__ == '__main__':
    print('Any developer who want to use this module, explicityly call add method')
    print('2 + 3 =', add(2, 3))