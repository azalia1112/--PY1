list_numbers = [2, -93, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
max_chy = 0
for current_chy in list_numbers:
    if current_chy > max_chy:
        max_chy = current_chy
num = list_numbers.index(max_chy)
list_numbers[num], list_numbers[-1] = list_numbers[-1], list_numbers[num]
print(list_numbers)

# TODO Оформить решение


