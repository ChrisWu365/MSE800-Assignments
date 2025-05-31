# This is staging branch
keys = ['a', 'b', 'c']
values = [1, 2]
dictionary = {k:v for k, v in zip(keys, values)}
print(dictionary)

dictionary3 = zip(keys, values)
print(tuple(dictionary3))

dictionary2 = {'d':4}
merged_dict = {**dictionary, **dictionary2}
print(merged_dict)

dict1 = {'a': 1, 'b': 4}
dict2 = {'b': 3, 'c': 3}
dict3 = {'d': 4, 'e': 5}
merge_dict123 = {**dict1, **dict2, **dict3}
print(merge_dict123)