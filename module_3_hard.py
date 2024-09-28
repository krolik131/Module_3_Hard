data_structure = [  [1, 2, 3],  {'a': 4, 'b': 5},  (6, {'cube': 7, 'drum': 8}),  "Hello",  ((), [{(2, 'Urban', ('Urban2', 35))}])]
sum_= 0
def calculate_structure_sum(data_structure):
    if isinstance(data_structure, list):
        function_for_collection(data_structure)
    elif isinstance(data_structure, int):
       global sum_
       sum_ = sum_ + data_structure

    elif isinstance(data_structure, dict):
       sum_ = sum_ + sum(data_structure.values())

       for i in data_structure:
           sum_ = sum_ + len(i)

    elif isinstance(data_structure, str):
        sum_ = sum_ + len(data_structure)

    elif isinstance(data_structure, tuple):
        function_for_collection(data_structure)

    elif isinstance(data_structure, set):
        function_for_collection(data_structure)
    return sum_

def function_for_collection(data_structure):
    for i in data_structure:
        calculate_structure_sum(i)

result = calculate_structure_sum(data_structure)
print(result)
