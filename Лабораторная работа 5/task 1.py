from pprint import pprint


def system_calc(number_list: list) -> list:
    list_dict = []
    for i in number_list:
        keylist = ['bin', 'dec', 'oct', 'hex']
        dict_of_number = dict.fromkeys(keylist)
        dict_of_number['bin'] = bin(i)
        dict_of_number['dec'] = i
        dict_of_number['oct'] = oct(i)
        dict_of_number['hex'] = hex(i)
        list_dict.append(dict_of_number)
    return list_dict


random_ = range(16)
pprint(system_calc(random_))
        # TODO решить с помощью list comprehension и распечатать его
