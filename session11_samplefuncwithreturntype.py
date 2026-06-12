# def sampleFunc(name):
#     if name[0]=='A':
#         return 'Alpha'
#     return 'Beta'
#create multiple paths for a function to return different values based on the input

#if name = int raise value error
#print(sampleFunc('Ailip'))  
# 
def sampleFunc(value):
  return 10 if value > 0 else -10  

print(sampleFunc(-2))

# check all the exceptions