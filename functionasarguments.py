employees=[
    {'name':'dilip', 'salary': 50000},
    {'name':'suresh', 'salary': 60000},
    {'name':'ajay', 'salary': 55000}

    ]

def get_salary(emp):
    return emp['salary']

# print(get_salary(employees[0]))

sorted_employees=sorted(employees, key=get_salary)
print(sorted_employees)    