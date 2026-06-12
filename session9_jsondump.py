# json.dump() method is used to convert a python object into a json string and stores in a file.
import json
import os
myDetails={'name':'dilip', 'city':'Bangalore'}
folderPath=r'C:\python_learning\python_learning'
fileName='newoutput.json'
if os.path.exists(folderPath):
    print(True)
#join is equal to concat in sql
fullPath=os.path.join(folderPath,fileName)
print(fullPath)
with open(fullPath, 'w') as f:
     json.dump(myDetails, f)