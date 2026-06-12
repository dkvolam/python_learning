from dictionary_definitions import add, sub, mul
from dictionary_data import data1

function_map = {
    "add": add,
    "sub": sub,
    "mul": mul
}

for key, value in data1.items():
    if value:
        function_map[key]()



