def get_simple_numbers(min, max):
    simple_numbers = []
    if min <= 3:
        if max >= 3:
            simple_numbers.append(3)
            min = 4
            for number in range(min, max+1):
                k = 0
                for i in range(2, number // 2+1):
                    if (number % i == 0):
                        k = k+1
                if (k <= 0):
                    simple_numbers.append(number)
    return simple_numbers if simple_numbers else "Простых чисел нет"

print(get_simple_numbers(1, 11))