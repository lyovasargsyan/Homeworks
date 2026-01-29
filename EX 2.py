dict_1 = {1: 'red', 2: 'green', 3: 'black', 4: 'white', 5: 'black'}
dict_2 = {}
for value in dict_1.values():
    dict_2[value] = len(value)


print(dict_2)