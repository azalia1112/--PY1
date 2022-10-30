def delete(list_, index=None):
    if index is None:
        list_1 = list_[:-1]
        return list_1
    elif index < 0:
        list_half1 = list_[:len(list_) + index]
        list_half2 = list_[len(list_) + index + 1:]
        return list_half1 + list_half2
    else:
        list_1_half1 = list_[:index]
        list_2_half2 = list_[index + 1:]
        return list_1_half1 + list_2_half2
    ...  # TODO реализовать функцию удаления элемента из списка по индексу


print(delete([0, 0, 1, 2], index=0))  # [0, 1]
print(delete([0, 1, 1, 2, 3], index=1))  # [0, 1, 2]
print(delete([0, 1, 2, 3, 4, 4]))  # [0, 1, 2, 3]
