import random

number_of_integers = 23
max_integer = 10
min_integer = -10
requested_sum = 0
list_of_integers = [random.randint(min_integer, max_integer) for i in range(number_of_integers)]

print(list_of_integers)

integer_pairs = []

for integer_x in range(number_of_integers):
    for integer_y in range(number_of_integers):
        if integer_x != integer_y:
            list_of_integers_x = list_of_integers[integer_x]
            list_of_integers_y = list_of_integers[integer_y]
            if (list_of_integers_x + list_of_integers_y) == requested_sum:
                integer_pairs.append((list_of_integers_x, list_of_integers_y))

print(integer_pairs)
