'''to find max salary' from a list of dictionaries


employees = [
    {"id": 1, "name": "Dilip", "salary": 7000, "department": "IT"},
    {"id": 2, "name": "Sam", "salary": 5000, "department": "HR"},
    {"id": 3, "name": "John", "salary": 9000, "department": "IT"},
    {"id": 4, "name": "Sara", "salary": 4000, "department": "Finance"}
]

print(len(employees))
max_sal=0

for i in range(len(employees)):
    if employees[i]['salary'] > max_sal:
        max_sal=employees[i]['salary']
print(max_sal)
'''

max_sal = 