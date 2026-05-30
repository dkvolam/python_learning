#increase steps at every func and print steps at the end of the day
steps=0
def enterOffice():
    global steps
    steps+=1
    print('welcome to office and step count is', steps)
def drinkTea():
    global steps
    steps+=1
    print('drinking tea and step count is', steps)
def meetBuddies():
    global steps
    steps+=1
    print('meeting buddies and step count is', steps)
def reachOdc():
    global steps
    steps+=1
    print('reaching odc and step count is', steps)   
def doWorkk():
    global steps
    steps+=1
    print('doing work and step count is', steps)
def breakForLunch():
    global steps
    steps+=1
    print('taking break for lunch and step count is', steps)

enterOffice()
drinkTea()
meetBuddies()
reachOdc()
doWorkk()
breakForLunch()
print('total steps taken in the day is', steps)
