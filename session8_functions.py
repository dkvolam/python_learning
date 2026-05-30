#id card should be numeric use isinstance() method to check the type of id card
# arugment for enteroffice and punch card should be same
#order of execution should fail if enteroffice is not executed before punchidcard
def enterOffice(idCard):
    if punchIdCard(idCard):
        print('welcome to office')
    else:
        print('you are not allowed to enter the office')
#enterOffice(False) # boolean syntax

def punchIdCard(idCard):
    if doorOpen(idCard):
        return True
    else:
        return False

def doorOpen(idCard):
    if isinstance(idCard, (int,float)):
        return True
    else:
        return False
    
enterOffice('abc')    
#punchIdCard('abc')