#from unicodedata import name


def enterDistrict(name):
    '''This name should contain 3 vowels, if exists it should return district name
    otherwise not a valid disctric should returned'''
    vowels = 'aeiou'
    count = 0
    for char in name:
        if char in vowels:
            count += 1
    if count == 3:
        return name
    else:
        return "Not a valid district"

def checkBackwardDistrict(name):
    '''step 1: create static dictionary, and check if the vlaue exists in dict then return district name
      This name should contain 3 vowels, if exists it should return district name
'''

    cities={'adilabad': 'not backward', 'delhiu': 'backword' }
    if name in cities.keys():
        return cities[name]
    else:
        return "Not a valid district"
    
return_value = enterDistrict('adilabad')
print(return_value)
return_value1 = checkBackwardDistrict('delhiu')
print(return_value1)