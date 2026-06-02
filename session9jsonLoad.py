'''most useful method, load is most useful method
it is used to read json file and convert it to python dict object'''

# replace dict vlaues with other vlaues and practice
import json
with open(r'C:\python_learning\python_learning\newoutput.json', 'r') as f:
    data=json.load(f)
# print(type(data))
# print(len(data))
# print(data[0])
for i in range(len(data)):
     if len(data[i]['roles']) > 1:
        print(data[i]['roles'][1])

# first_user = data[0]
# print(first_user)