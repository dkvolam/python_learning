'''
Mode	Meaning
"r"	Read
"w"	Write (overwrite)
"a"	Append
"x"	Create new file
"rb"	Read binary
"wb"	Write binary
"r+"	Read + write'''
import json
import os
source_path='C:\python_learning\python_learning'
destination_path='C:\python_learning\python_learning'
source_file_name='newoutput.json'
target_file_name='newoutput_copy.json'
source_full_path=os.path.join(source_path,source_file_name)
target_full_path=os.path.join(destination_path,target_file_name)
if os.path.exists(source_full_path):
    with open(source_full_path, 'r') as f:
        data=json.load(f)
    with open(target_full_path, 'w') as f:
        json.dump(data, f)


