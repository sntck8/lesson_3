def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params(5, 'String')
print_params(7, None, False)
print_params(666)
print_params()

values_list = [18, "sTrOkA", 111.222]
values_dict = {"a": 2, "b": "Строчка", "c": False }

print_params(*values_list)
print_params(**values_dict)

values_list_2 =[44, "Forty_four"]

print_params(*values_list_2, 42)
print("----------------------")
print("Все параметры работают")
