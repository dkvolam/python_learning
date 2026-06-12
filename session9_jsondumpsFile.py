# json.dumps() method is used to convert a python object into a json string and stores in a merory or string.
import json
'''json.dumps is used to convert a python object into a json string 
it can be seen by doing type before and after using dumps method'''
myDetails={'name':'dilip', 'age':'40', 'city':'Bangalore'}
print(type(myDetails))
#this is like converting datatype in sql like to_char is equal to json.dumps in python
jsontostring=json.dumps(myDetails)
print(type(jsontostring))
print(jsontostring)





