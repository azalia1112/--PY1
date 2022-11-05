from random import randint


def get_unique_list_numbers() -> list[int]:
    random_numbers = []
    while len(set(random_numbers)) != 15:
        random_numbers.append(randint(-10, 10))
    return set(random_numbers)


    ...  # TODO написать функцию для получения списка уникальных целых чисел


list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
