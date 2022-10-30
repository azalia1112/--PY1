def get_count_char(str_):
    DEFAULT_COUNT = 0
    dict_ = {}
    word_list = str_.split(" ")
    str_new = "".join(word_list)
    unique_list = []
    if not str_new.isalpha():
        for sym in list(str_new):
            if str(sym).isalpha():
                unique_list.append(sym)
    empty_str = "".join(unique_list).lower()
    LIST_ = list(empty_str)
    unique_list = list(empty_str)
    unique_list.sort()
    for sym in unique_list:
        dict_.setdefault(sym, DEFAULT_COUNT)
    for sym in LIST_:
       dict_[sym] = dict_.get(sym, DEFAULT_COUNT) + 1
    return dict_


def percent(str_, dict_):
    DEFAULT_COUNT = 0
    dict_2 = {}
    dict_ = dict(dict_)
    sum_sym = sum(get_count_char(str_).values())
    for key, value in dict_.items():
        if key in get_count_char(str_):
            count_sym = get_count_char(str_).get(key)
            persent_ = (count_sym / sum_sym) * 100
            dict_2.setdefault(key, DEFAULT_COUNT)
            dict_2[key] = dict_2.get(key, DEFAULT_COUNT) + persent_
        else:
            dict_2.setdefault(key, DEFAULT_COUNT)
    return dict_2


 # TODO посчитать количество каждой буквы в строке в аргументе str_


main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))
dict_percent = {
    "p": 0,
    "а": 0,
    "с": 0,
    "9": 0,
    "t": 0,
    "в": 0
}
print(percent(main_str, dict_percent))

