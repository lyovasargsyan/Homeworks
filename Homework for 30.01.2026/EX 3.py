def dictFilter(dict_1):
    dict_2 = {}
    for key, values in dict_1.items():
        lst = []
        for i in values:
            if i%2!=0:
                lst.append(i)
        dict_2[key] = lst
    
    return dict_2

dict1 = {'a': [1, 8, 3, 7, 2], 'b': [12, 4, 8, 4], 'c': [9, 9, 2, 8, 5]}
print(dictFilter(dict1))