import csv
with open('C:\python_learning\python_learning\student.csv',newline='') as f:
    reader=csv.reader(f,delimiter=',',quotechar='|')
    for row in reader:
        print(',' .join(row))

## practice writing csv

