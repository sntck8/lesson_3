data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]

def calculate_structure_sum(data_structure):
  sum_nums = 0
  sum_strs = 0

  def recursion(data):
    nonlocal sum_nums, sum_strs
    if isinstance(data, (list, tuple, set)):
      for item in data:
        recursion(item)
    if isinstance(data, dict):
      for value in data.values():
        recursion(value)
      for key in data.keys():
        recursion(key)
    if isinstance(data, (int, str)):
      if isinstance(data, int):
        sum_nums += data
      if isinstance(data, str):
        sum_strs += len(data)

  recursion(data_structure)
  return sum_nums + sum_strs

result = calculate_structure_sum(data_structure)
print("Сумма всех чисел и строк:", result)
