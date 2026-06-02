''' json.loads method takes string as input and  converts json string to python dict object'''
# import json
# str1='{"id1":"dilip", "loc":"hyderabad"}'
# print(type(str1))
# str1ToDict=json.loads(str1)
# print(type(str1ToDict))
# print(str1ToDict)


import json
str1='{"id1":"dilip", "loc":"hyderabad"}'
print(type(str1))
dict1=json.loads(str1)
print(type(dict1))
print(dict1)


