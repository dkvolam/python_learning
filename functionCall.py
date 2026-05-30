
import dilip


def firstFunc():
    '''This is first function'''
    print('secondFunc created by firstFunc')
    secondFunc()
def secondFunc():
    '''This is second function'''
    print('This is second function')
    return 'Second Function'
def thirdFunc():
    '''This is third function'''
    print('firstFunc created by thirdFunc')
    firstFunc()
def fourthFunc():
    '''This is fourth function'''
    thirdFunc()

def main():
    firstFunc()
   
print(thirdFunc.__doc__)


 