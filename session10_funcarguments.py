filename=input("enter your file name\n")
def readCsv(filename):
    print('reading csv file',filename)
def readExcel(filename):
    print('reading excel file', filename)
def readPdf(filename):
    print('reading pdf file',filename)
def execute(a,file):
    return a(file)
#use split func and check the extension of filename 
# and based on that call the function
#use split function on string
str1=filename.split('.')

if str1[1]=='csv':
    execute(readCsv,filename)
elif str1[1]=='xls':
    execute(readExcel,filename)
elif str1[1]=='pdf':
    execute(readPdf,filename)



