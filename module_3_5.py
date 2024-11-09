def get_multiplied_digits(number):
    str_number = str(number)
    first = int(str_number[0])

    while len(str_number) > 1:
        return first * get_multiplied_digits(int(str_number[1:]))
    else:
        if len(str_number) <= 1:
            return first

print(get_multiplied_digits("40203"))