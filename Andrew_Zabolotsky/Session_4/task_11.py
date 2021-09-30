def combine_dicts(*dicts):
    Main_dict = {}
    for i in dicts:
        for key in i.keys():
            if key in Main_dict:
                Main_dict[key] += i[key]
            else:
                Main_dict[key] = i[key]
    return Main_dict

dict_1 = {'a': 100, 'b': 200}
dict_2 = {'a': 200, 'c': 300}
dict_3 = {'a': 300, 'd': 100}
print(combine_dicts(dict_1, dict_2, dict_3))
